# 🎓 Elimu AI — CBC Intelligent Tutoring System

> **AI-powered offline-ready tutor for marginalized learners in Kenya**
> University of Eastern Africa, Baraton | AI Group 19
> Delfine Achieng · Geoffrey Njenga · Chepchumba Faith

---

## 📌 Project Overview

Elimu AI addresses the educational gap in arid, remote, and conflict-affected regions of Kenya (Turkana, Garissa, Mandera, Marsabit Counties). It is an offline-capable AI tutoring system that:

- Uses a **Random Forest Classifier** (supervised ML) to classify student performance
- Covers **Mathematics, English, and Kiswahili** — aligned to the Kenyan CBC curriculum
- Works **without internet** via a locally embedded model (offline-first architecture)
- Is hosted on **Hugging Face Spaces** (free cloud) for when connectivity is available
- Runs on **solar-powered, low-cost devices** (no heavy compute required)

---

## 🤖 Machine Learning Algorithm

**Algorithm: Random Forest Classifier** *(Breiman, Leo. 2001)*

| Metric | Value |
|---|---|
| Test Accuracy | **100.00%** |
| Validation Accuracy | **99.92%** |
| 5-Fold CV Mean | **99.96% ± 0.03%** |
| Training Samples | 5,600 |
| Performance Classes | Beginner · Intermediate · Advanced |

### Features Used
| Feature | Description |
|---|---|
| `grade` | Student's CBC grade level (1–6) |
| `subject_enc` | Subject (Math / English / Kiswahili) |
| `topic_enc` | Curriculum topic (encoded) |
| `difficulty_enc` | Easy / Medium / Hard |
| `num_questions` | Questions attempted |
| `correct_answers` | Number answered correctly |
| `incorrect_answers` | Number answered incorrectly |
| `accuracy_rate` | Proportion correct |
| `total_score` | Score out of 100 |
| `avg_time_seconds` | Average time per question |
| `score_per_question` | Score efficiency ratio |
| `efficiency` | Accuracy / time ratio |

### Data Split
- **70%** Training (5,600 records)
- **15%** Validation (1,200 records)
- **15%** Test (1,200 records)

---

## 🗂️ Project Structure

```
elimu-ai/
├── data/
│   ├── generate_dataset.py     # CBC dataset generator (8,000 records)
│   └── cbc_assessment_data.csv # Generated dataset
├── model/
│   ├── train_model.py          # Random Forest training pipeline
│   ├── random_forest_model.pkl # Trained model (binary)
│   ├── encoders.pkl            # Label encoders
│   └── metadata.json           # Model metrics & config
├── api/
│   ├── main.py                 # FastAPI REST API
│   └── requirements.txt        # Python dependencies
├── frontend/
│   └── index.html              # Child-friendly tutor UI
├── notebooks/
│   └── Elimu_AI_Training.ipynb # Google Colab notebook
├── app.py                      # Hugging Face Spaces entry point
└── README.md
```

---

## 🚀 Quick Start

### Option A — Run locally (your laptop)

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/elimu-ai.git
cd elimu-ai

# 2. Install dependencies
pip install fastapi uvicorn scikit-learn numpy pandas pydantic

# 3. Generate dataset and train model
python data/generate_dataset.py
python model/train_model.py

# 4. Start the API server
uvicorn api.main:app --reload --port 8000

# 5. Open frontend/index.html in your browser
#    Update API_URL in index.html to: http://localhost:8000
```

### Option B — Train on Google Colab (FREE, no powerful laptop needed)

1. Go to [Google Colab](https://colab.research.google.com)
2. Upload `notebooks/Elimu_AI_Training.ipynb`
3. Run all cells in order
4. Download the trained `.pkl` files and commit to your repo

### Option C — Deploy API to Hugging Face Spaces (FREE cloud hosting)

See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API info |
| GET | `/health` | Health check |
| POST | `/predict` | Classify student performance |
| POST | `/quiz` | Get CBC quiz questions |
| GET | `/subjects` | List available subjects |
| GET | `/model-info` | Model metadata |

### Example — Predict Performance

```bash
curl -X POST "https://YOUR-SPACE.hf.space/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "grade": 4,
    "subject": "Mathematics",
    "topic": "Addition",
    "difficulty_level": "Medium",
    "num_questions": 10,
    "correct_answers": 8,
    "avg_time_seconds": 25
  }'
```

**Response:**
```json
{
  "performance_level": "Advanced",
  "confidence": 0.97,
  "score": 80.0,
  "recommendation": {
    "message": "Hongera sana! Excellent work!",
    "activities": ["Challenge yourself with hard questions", "..."]
  }
}
```

---

## 📊 Dataset

The dataset was synthetically generated to mirror real CBC assessment patterns:

- **8,000 labeled records** across 1,000 unique student IDs
- **3 subjects**: Mathematics, English, Kiswahili
- **10 topics per subject** drawn from the official CBC curriculum
- **3 difficulty levels**: Easy, Medium, Hard
- **3 performance labels**: Beginner, Intermediate, Advanced
- Class balancing applied via `class_weight='balanced'`

---

## 🛠️ Deployment Architecture

```
[Student Device]          [Cloud — Hugging Face Spaces]
  Solar-powered   <──────>  FastAPI + Random Forest
  Low-cost tablet          (free, always-on hosting)
  frontend/index.html
       │
       │ (offline fallback)
       └──> Embedded JS question bank + local classification
```

The system is **offline-first**: if no internet is available, the embedded JavaScript fallback provides full quiz and classification functionality with no cloud dependency.

---

## 📚 References

- Breiman, Leo. (2001). Random forests. *Machine Learning*, 45(1), 5–32.
- UNESCO. (2022). *Education in emergencies: Strengthening resilience in crisis-affected regions.*
- UNICEF. (2021). *Education disruption and recovery in ASALs in Kenya.*
- VanLehn, Kurt. (2011). The relative effectiveness of human tutoring, ITS, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221.
- World Bank. (2023). *Kenya education sector analysis report.*

---

## 👥 Team

| Name | Role |
|---|---|
| Delfine Achieng | ML Model & Data Pipeline |
| Geoffrey Njenga | API Development & Deployment |
| Chepchumba Faith | Frontend & Curriculum Integration |

**Institution:** University of Eastern Africa, Baraton
**Course:** Artificial Intelligence
**Assignment:** Group 19, Assignment 1
