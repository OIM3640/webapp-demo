import os

import requests
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")


# ── Homepage ──


@app.route("/")
def index():
    return render_template("index.html")


# ── Hello ──


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


# ── AI Assistant (OpenAI API) ──


@app.get("/ai")
def ai_get():
    return render_template("ai.html")


@app.post("/ai")
def ai_post():
    prompt = request.form.get("prompt", "").strip()
    if not prompt:
        flash("Please enter a question.", "error")
        return redirect(url_for("ai_get"))

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        flash("OpenAI API key is not configured.", "error")
        return redirect(url_for("ai_get"))

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
        )
        answer = response.output_text
    except Exception as e:
        flash(f"API error: {e}", "error")
        return redirect(url_for("ai_get"))

    return render_template("ai.html", prompt=prompt, answer=answer)


# ── Message Board (OIM Teaching API) ──

OIM_API_BASE = "https://oim.108122.xyz"


@app.route("/messages")
def messages_page():
    try:
        resp = requests.get(f"{OIM_API_BASE}/messages", timeout=5)
        resp.raise_for_status()
        messages = resp.json()
    except requests.RequestException:
        flash("Could not load messages.", "error")
        messages = []
    return render_template("messages.html", messages=messages)


@app.post("/messages")
def send_message():
    name = request.form.get("name", "").strip()
    body = request.form.get("body", "").strip()

    if not name or not body:
        flash("Name and message are both required.", "error")
        return redirect(url_for("messages_page"))

    if len(body) > 140:
        flash("Message must be 140 characters or fewer.", "error")
        return redirect(url_for("messages_page"))

    try:
        resp = requests.post(
            f"{OIM_API_BASE}/message",
            json={"name": name, "body": body},
            timeout=5,
        )
        resp.raise_for_status()
        flash("Message sent!", "success")
    except requests.RequestException:
        flash("Could not send message.", "error")

    return redirect(url_for("messages_page"))


# ── Weather (OpenWeather API) ──


@app.get("/weather")
def weather_get():
    return render_template("weather.html")


@app.post("/weather")
def weather_post():
    city = request.form.get("city", "").strip()
    if not city:
        flash("Please enter a city name.", "error")
        return redirect(url_for("weather_get"))

    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        flash("OpenWeather API key is not configured.", "error")
        return redirect(url_for("weather_get"))

    try:
        resp = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=5,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        flash(f'Could not fetch weather for "{city}".', "error")
        return redirect(url_for("weather_get"))

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].capitalize(),
    }
    return render_template("weather.html", city=city, weather=weather)


# ── Astronauts (Open Notify API) ──


@app.route("/astronauts")
def astronauts():
    try:
        resp = requests.get("http://api.open-notify.org/astros.json", timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        flash("Could not fetch astronaut data.", "error")
        data = {"number": 0, "people": []}

    return render_template(
        "astronauts.html",
        count=data["number"],
        people=data["people"],
    )


# ── Error Handling ──


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
