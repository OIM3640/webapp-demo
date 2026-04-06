# Deploy to Render

[Render](https://render.com/) offers a free tier for web services — great for class projects and demos.

## Step 1 — Prepare your repository

Make sure these files are committed to your repo:

- `requirements.txt` — Python dependencies
- `app.py` — your Flask application

> **Important:** Do NOT commit your `.env` file. Environment variables are set through the Render dashboard (Step 4).

## Step 2 — Create a Render account

Sign up at [render.com](https://render.com/) with your GitHub account.

## Step 3 — Create a new Web Service

1. From the [Render Dashboard](https://dashboard.render.com/), click **New** > **Web Service**.
2. Connect your GitHub repository.
3. Configure the service:

| Setting | Value |
|---------|-------|
| **Name** | `flask-demo` (or any name you like) |
| **Region** | Ohio (US East) or closest to you |
| **Branch** | `master` (or `main`) |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | **Free** |

4. Click **Deploy Web Service**.

## Step 4 — Set environment variables

1. In your service's dashboard, click **Environment** in the left sidebar.
2. Click **+ Add Environment Variable** and add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | any random string |
| `OPENAI_API_KEY` | your OpenAI API key |
| `OPENWEATHER_API_KEY` | your OpenWeather API key |

3. Click **Save, rebuild, and deploy**.

> **Tip:** You can also click **Add from .env** to import from a local `.env` file.

## Step 5 — Visit your app

Once the deploy finishes, your app will be live at:

```
https://flask-demo.onrender.com
```

(The exact URL depends on the name you chose.)

## Updating your app

Every push to your linked branch automatically triggers a new build and deploy. Just `git push` and Render handles the rest.

## Free tier limitations

- **Spin-down:** Free services sleep after 15 minutes of inactivity. The first request after sleeping takes ~30–60 seconds to respond.
- **750 hours/month:** Shared across all free services in your workspace. Plenty for a single demo app.
- **No persistent disk:** Local filesystem resets on every deploy and spin-down.
- **Single instance:** No horizontal scaling.

For a class project, these limitations are not an issue.
