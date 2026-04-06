# Deploy to PythonAnywhere

[PythonAnywhere](https://www.pythonanywhere.com/) offers a free tier that can host one web app.

## Step 1 — Create an account

Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/). The free "Beginner" plan is sufficient.

## Step 2 — Upload your code

Open a **Bash console** from the PythonAnywhere dashboard and clone your repo:

```bash
git clone https://github.com/OIM3640/webapp-demo.git
```

## Step 3 — Create a virtual environment

PythonAnywhere does not support `uv`, so use the built-in `venv` and `pip`:

```bash
cd webapp-demo
python3 -m venv .venv
source .venv/bin/activate
pip install flask requests python-dotenv openai
```

## Step 4 — Set up environment variables

Create a `.env` file in your project directory:

```bash
cp .env.example .env
nano .env  # or use the Files tab in the dashboard
```

Fill in your API keys.

## Step 5 — Configure the web app

1. Go to the **Web** tab in the PythonAnywhere dashboard.
2. Click **Add a new web app**.
3. Choose **Manual configuration** (not "Flask").
4. Select **Python 3.12** (or the version matching your project).

### Set the virtualenv path

In the **Virtualenv** section, enter:

```
/home/YOUR_USERNAME/webapp-demo/.venv
```

### Edit the WSGI file

Click the link to the WSGI configuration file and **replace its entire contents** with:

```python
import sys
import os

# Add your project directory to the path
project_home = "/home/YOUR_USERNAME/webapp-demo"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables from .env
os.chdir(project_home)
from dotenv import load_dotenv
load_dotenv(os.path.join(project_home, ".env"))

# Import Flask app
from app import app as application
```

Replace `YOUR_USERNAME` with your PythonAnywhere username.

## Step 6 — Reload and test

Click **Reload** on the Web tab. Your app should be live at:

```
https://YOUR_USERNAME.pythonanywhere.com
```

## Updating your app

When you push new changes to GitHub:

```bash
cd ~/webapp-demo
git pull
```

Then click **Reload** on the Web tab.

## Limitations of the free tier

- One web app only
- Custom domains not available
- App may be slow after periods of inactivity
- 512 MB disk space
- Outbound internet access is restricted to an allowlist of sites (OpenWeather and OpenAI are included)
