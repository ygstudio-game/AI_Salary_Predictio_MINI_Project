# AI-Based Employee Salary Prediction System Using Cloud Computing

A simple, robust Machine Learning application deployed on the cloud to estimate an employee's annual salary based on demographic and professional parameters. Developed for the Third Year (TE) Cloud Computing (CC) Mini Project at **PCCOER, Ravet, Pune** (AY 2026–27).

---

## 1. Project Overview

In the modern corporate job market, salary determination often suffers from lack of transparency and subjective bias. This project implements an **AI-Based Employee Salary Predictor** that applies a supervised **Linear Regression** model wrapped in a Scikit-learn Pipeline, hosted on **Google Cloud Run** using a containerized **Streamlit** web interface.

### Project Details
- **Subject:** Cloud Computing (CC) Mini Project
- **Group:** Group C
- **Team Members:**
  1. **TECOA57** — Yadnyesh Borole
  2. **TECOA55** — Om Borkar
  3. **TECOA47** — Sumit Bhoye
  4. **TECOA65** — Dhananjay Chavan
- **Institute:** Pimpri Chinchwad College of Engineering & Research (PCCOER), Ravet, Pune

---

## 2. Problem Statement

Manual salary benchmarking is time-consuming, prone to human inconsistency, and often opaque. Employees and hiring teams frequently lack an instant, objective benchmark to evaluate compensation packages based on measurable criteria. 

**Objective:** To design, train, evaluate, and deploy a lightweight, explainable machine learning model on a scalable cloud platform that predicts annual compensation in INR (₹) based on key professional indicators.

---

## 3. Key Objectives

- Develop a synthetic educational dataset reflecting realistic salary trends with natural statistical variance.
- Build an end-to-end preprocessing and ML training pipeline utilizing Scikit-learn.
- Evaluate the model using standard regression metrics (MAE, MSE, RMSE, and $R^2$).
- Build an intuitive, interactive web interface using Streamlit.
- Package the entire application inside a Docker container.
- Deploy the container on Google Cloud Run to demonstrate serverless cloud elasticity and global accessibility.

---

## 4. Features

- **Intuitive Web UI:** Clean, responsive user interface built in Streamlit.
- **Instant Estimation:** Real-time salary calculation presented in Indian Rupees (₹).
- **Categorical & Numerical Handling:** Integrated `ColumnTransformer` with `OneHotEncoder`.
- **Explainable Model:** Linear regression coefficients provide clear reasoning during viva examinations.
- **Serverless Cloud Deployment:** Packaged into an OCI-compliant container deployed on Google Cloud Run.
- **Zero Idle Cost:** Cloud Run scales to zero instances when no requests are being processed.

---

## 5. Technology Stack

| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Language** | Python 3.12 | Core development language |
| **Data Processing** | Pandas, NumPy | Data ingestion, tabular manipulation, array calculations |
| **Machine Learning** | Scikit-learn | Pipeline, ColumnTransformer, OneHotEncoder, Linear Regression |
| **Serialization** | Joblib | Saving and loading `salary_model.pkl` |
| **Web Framework** | Streamlit | Frontend input widgets, metric displays, sidebar |
| **Visualization** | Matplotlib | Salary vs experience & prediction accuracy plots |
| **Containerization** | Docker | Creating lightweight container image |
| **Cloud Hosting** | Google Cloud Run | Serverless container execution |

---

## 6. Machine Learning Algorithm & Pipeline

The system uses **Multiple Linear Regression**, modeling the linear relationship between input attributes and the target salary:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_k x_k + \epsilon$$

### Feature Schema:
1. `age` (Numerical: 21 to 60)
2. `years_experience` (Numerical: 0 to 25)
3. `education_level` (Categorical: `Bachelors`, `Masters`, `PhD` — one-hot encoded)
4. `job_level` (Categorical: `Junior`, `Mid`, `Senior`, `Manager` — one-hot encoded)
5. `weekly_hours` (Numerical: 35 to 55)

**Target Variable:** `salary` (Continuous, in ₹ INR)

---

## 7. Dataset Details

- **File:** `data/employee_salary_data.csv`
- **Total Samples:** 600 records
- **Split:** 80% Training (480 records), 20% Testing (120 records)
- **Nature:** Synthetic educational dataset generated specifically for classroom and laboratory demonstration. No personal identifiable information (PII) is included.

---

## 8. Measured Evaluation Metrics

Model trained and validated on a held-out test set (`random_state=42`):

| Metric | Measured Value |
| :--- | :--- |
| **Mean Absolute Error (MAE)** | ₹47,097.10 |
| **Mean Squared Error (MSE)** | 3,690,312,169.22 |
| **Root Mean Squared Error (RMSE)** | ₹60,747.94 |
| **Coefficient of Determination ($R^2$)** | 0.9870 (98.7%) |

---

## 9. Project Directory Structure

```
employee-salary-predictor/
├── app.py                      # Streamlit application
├── train_model.py              # ML training script
├── make_dataset.py             # Dataset generation script
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build instructions
├── README.md                   # This documentation
├── data/
│   └── employee_salary_data.csv# Dataset
├── model/
│   └── salary_model.pkl        # Serialized pipeline
└── report/
    ├── architecture.md         # System architecture details
    ├── testing.md              # Test plan and test cases
    ├── viva_questions.md       # Viva Voce preparation Q&A
    ├── presentation_outline.md # 10-12 slide deck outline
    ├── screenshot_checklist.md # Screenshot submission guide
    ├── test_results.txt        # 5 verified test cases
    └── training_output.txt     # Training log & metrics
```

---

## 10. Installation & Local Setup

### Prerequisites
- Python 3.10+ installed
- Git (optional)
- Docker (optional, for container testing)

### Step 1: Clone or Navigate to Directory
```bash
cd employee-salary-predictor
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: (Optional) Re-train the Model
```bash
python train_model.py
```

### Step 4: Run the Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 11. Example Usage & Test Cases

| Test Case | Inputs | Predicted Salary |
| :--- | :--- | :--- |
| **TC1: Mid-level** | Age: 30, Exp: 5, Edu: Masters, Level: Mid, Hours: 40 | **₹9,96,300** |
| **TC2: Junior** | Age: 22, Exp: 0, Edu: Bachelors, Level: Junior, Hours: 40 | **₹2,61,146** |
| **TC3: Senior** | Age: 50, Exp: 25, Edu: Masters, Level: Senior, Hours: 45 | **₹25,60,662** |
| **TC4: Manager** | Age: 30, Exp: 5, Edu: Masters, Level: Manager, Hours: 40 | **₹16,40,358** |
| **TC5: PhD** | Age: 30, Exp: 5, Edu: PhD, Level: Mid, Hours: 40 | **₹11,03,917** |

---

## 12. Docker & Cloud Deployment

### Local Docker Build & Run
```bash
# Build Docker image
docker build -t employee-salary-predictor .

# Run container locally
docker run -p 8080:8080 -e PORT=8080 employee-salary-predictor
```
Navigate to `http://localhost:8080`.

### Deploying to Google Cloud Run
```bash
# 1. Authenticate with GCP
gcloud auth login

# 2. Select Project
gcloud config set project [YOUR_PROJECT_ID]

# 3. Deploy directly to Cloud Run
gcloud run deploy salary-predictor \
  --source . \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated
```

---

## 13. Limitations

- **Synthetic Data:** Model is trained on 600 synthetic records created for educational purposes.
- **Feature Set:** Does not account for geographical cost of living, company revenue, negotiation dynamics, or macroeconomic conditions.
- **Linearity Assumption:** Assumes linear feature-salary correlation, whereas real executive salaries often follow exponential tiers.

---

## 14. Future Scope

- Incorporate non-linear algorithms such as **Random Forest Regressor** or **XGBoost**.
- Introduce database persistence (e.g., Google Cloud Firestore or PostgreSQL) for logging prediction queries.
- Implement an automated CI/CD pipeline using GitHub Actions and Google Cloud Build.
- Integrate Explainable AI (SHAP / LIME) to illustrate feature contributions per prediction.

---

## 15. Disclaimer

This application is developed strictly for **academic and educational purposes** as part of an engineering mini-project. Predicted salaries are statistical estimations and should **not** be considered official compensation offers or used for actual corporate HR decisions.
