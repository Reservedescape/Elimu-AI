# 🚀 Deployment Guide — Elimu AI

## Step 1: Push to GitHub

### First time setup
```bash
cd elimu-ai

# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit: Elimu AI CBC Tutoring System"

# Create a new repo on github.com named 'elimu-ai', then:
git remote add origin https://github.com/YOUR_USERNAME/elimu-ai.git
git branch -M main
git push -u origin main
```

### After training the model (adds .pkl files)
```bash
git add model/random_forest_model.pkl model/encoders.pkl model/metadata.json
git add data/cbc_assessment_data.csv
git commit -m "Add trained Random Forest model and CBC assessment dataset"
git push
```

---

## Step 2: Train on Google Colab (Free GPU/CPU)

1. Go to **https://colab.research.google.com**
2. Click **File → Upload notebook**
3. Upload `notebooks/Elimu_AI_Training.ipynb`
4. In Cell 2, replace `YOUR_GITHUB_USERNAME` with your actual username
5. In Cell 7, add your GitHub email, name, and Personal Access Token
6. Click **Runtime → Run all**

The notebook will:
- Install all dependencies
- Clone your repo
- Generate the 8,000-record CBC dataset
- Train the Random Forest classifier
- Show evaluation plots
- Push the trained model back to GitHub

---

## Step 3: Deploy API to Hugging Face Spaces (Free)

### 3a. Create a Hugging Face account
Go to **https://huggingface.co** and sign up (free).

### 3b. Create a new Space
1. Click your profile → **New Space**
2. Space name: `elimu-ai`
3. SDK: **Docker** (or Gradio — but Docker is more flexible)
4. Visibility: **Public**

### 3c. Add a Dockerfile to your repo

Create a file called `Dockerfile` in your project root:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]
```

Then push it:
```bash
git add Dockerfile
git commit -m "Add Dockerfile for Hugging Face deployment"
git push
```

### 3d. Connect GitHub to Hugging Face
In your Space settings → **Repository** → link your GitHub repo `elimu-ai`.
Hugging Face will auto-build and deploy on every push.

### 3e. Get your Space URL
Your API will be live at:
```
https://YOUR_HF_USERNAME-elimu-ai.hf.space
```

---

## Step 4: Update Frontend with Your API URL

Open `frontend/index.html` and find this line near the bottom:
```javascript
const API_URL = "https://YOUR-USERNAME-elimu-ai.hf.space"; // ← update after deploy
```

Replace it with your actual Hugging Face Space URL:
```javascript
const API_URL = "https://delfine-elimu-ai.hf.space";  // example
```

Then push the update:
```bash
git add frontend/index.html
git commit -m "Update API URL to Hugging Face Space"
git push
```

---

## Step 5: Host the Frontend (Optional)

### Option A — GitHub Pages (Free)
1. Go to your repo on GitHub
2. Settings → Pages → Source: **Deploy from a branch**
3. Branch: `main` / Folder: `/frontend`
4. Your tutor UI will be live at: `https://YOUR_USERNAME.github.io/elimu-ai`

### Option B — Just open locally
Since the frontend is a single HTML file, you can just open `frontend/index.html`
directly in any browser — no server needed. This is the **offline mode**.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| API not responding | Check HF Space logs → Manage Space → Logs |
| Model not found | Make sure .pkl files are committed to GitHub |
| CORS error | Already handled in `api/main.py` with `allow_origins=["*"]` |
| Offline mode used | Normal! The frontend has a built-in fallback |
| Colab disconnects | Re-run from the dataset generation cell |

---

## Architecture Recap

```
GitHub Repo
    │
    ├── Triggers Hugging Face Space rebuild (auto-deploy)
    │        │
    │        └── FastAPI API (always-on, free)
    │                 │
    │                 ├── POST /predict  → Random Forest Classifier
    │                 └── POST /quiz     → CBC Question Bank
    │
    └── frontend/index.html
              │
              ├── Fetches questions + predictions from HF Space API
              └── Falls back to offline JS mode if no internet
```
