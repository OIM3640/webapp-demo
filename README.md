# Flask Demo

A collection of mini web apps that demonstrate core Flask concepts — routing, templates, forms, API integration, and environment variable management.

## Features

| Page | Route | Concepts |
|------|-------|----------|
| **Hello** | `/hello`, `/hello/<name>` | Dynamic routing, template variables |
| **AI Assistant** | `/ai` | Form POST, OpenAI API, `.env` secrets |
| **Message Board** | `/messages` | GET & POST to external API, flash messages |
| **Weather** | `/weather` | Form input → API call, API key management |
| **Astronauts** | `/astronauts` | Simple GET API, JSON parsing, table rendering |

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/OIM3640/webapp-demo.git
cd webapp-demo
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy the example file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```
SECRET_KEY=any-random-string-here
OPENAI_API_KEY=sk-...
OPENWEATHER_API_KEY=your-key-from-openweathermap.org
```

- **OpenAI API key**: provided via Canvas
- **OpenWeather API key**: sign up free at [openweathermap.org](https://openweathermap.org/api)

### 4. Run the app

```bash
flask run --debug
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Project Structure

```
webapp-demo/
├── app.py                 # Flask application (routes and logic)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── static/
│   └── style.css          # Stylesheet
├── templates/
│   ├── base.html          # Base template (nav + layout)
│   ├── index.html         # Homepage
│   ├── hello.html         # Hello page
│   ├── ai.html            # AI assistant
│   ├── messages.html      # Message board
│   ├── weather.html       # Weather lookup
│   ├── astronauts.html    # Astronauts in space
│   └── 404.html           # Custom error page
└── docs/
    ├── deploy-render.md           # Render deployment guide
    └── deploy-pythonanywhere.md   # PythonAnywhere deployment guide
```

## Key Concepts Demonstrated

- **Template inheritance** — `base.html` defines the layout; other templates extend it with `{% extends "base.html" %}`
- **Static files** — CSS loaded via `url_for('static', filename='style.css')`
- **Form handling** — GET to show form, POST to process input, redirect on error
- **Flash messages** — User feedback for errors and success
- **API integration** — `requests` library to call external APIs
- **Environment variables** — `python-dotenv` to load `.env` file; secrets never hardcoded
- **Error handling** — Custom 404 page, try/except around API calls

## Deployment

- [Deploy to Render](docs/deploy-render.md)
- [Deploy to PythonAnywhere](docs/deploy-pythonanywhere.md)
