# Mini Project Presentation Outline (12-Slide Deck)

This document provides a complete slide-by-slide structure for presenting the **AI-Based Employee Salary Prediction System Using Cloud Computing** during your college evaluation.

---

### Slide 1: Title & Team Introduction
- **Slide Title:** AI-Based Employee Salary Prediction System Using Cloud Computing
- **Sub-Header:** Third Year (TE) Cloud Computing Mini Project (Term-I, AY: 2026–27)
- **Institution:** PCET's Pimpri Chinchwad College of Engineering & Research (PCCOER), Ravet, Pune
- **Team Members:**
  - Yadnyesh Borole (TECOA57)
  - Om Borkar (TECOA55)
  - Sumit Bhoye (TECOA47)
  - Dhananjay Chavan (TECOA65)
- **Course Incharge / Guide:** `[Course Incharge Name]`
- **Suggested Visual:** College Logo + Modern Cloud Computing & AI graphic.

---

### Slide 2: Problem Statement & Motivation
- **Slide Title:** Problem Statement & Motivation
- **Key Bullet Points:**
  - Salary negotiation and compensation analysis often rely on subjective guesswork or manual job board browsing.
  - Lack of standardized, instant estimation benchmarks leads to compensation disparities.
  - Traditional desktop ML models remain confined to local environments and lack accessibility.
  - **Goal:** Build an accessible, cloud-native AI application that predicts estimated annual salary based on measurable professional criteria.
- **Suggested Visual:** Icon representing HR compensation / question mark over salary scale.

---

### Slide 3: Aim & Project Objectives
- **Slide Title:** Aim & Project Objectives
- **Aim:** To design, develop, and deploy an AI-based salary prediction system on a scalable cloud platform.
- **Key Objectives:**
  - Construct a structured, synthetic educational dataset with natural variance.
  - Implement a preprocessing pipeline handling numerical and categorical variables.
  - Train an explainable Multiple Linear Regression model with Scikit-learn.
  - Build an interactive web frontend using Streamlit.
  - Containerize using Docker and deploy to Google Cloud Run serverless platform.
- **Suggested Visual:** Numbered list with target completion icons.

---

### Slide 4: Proposed System Overview
- **Slide Title:** Proposed System Workflow
- **Key Bullet Points:**
  - **Inputs:** Age, Years of Experience, Education Level, Job Level, Weekly Working Hours.
  - **Processing Engine:** Scikit-learn Pipeline with `ColumnTransformer` (One-Hot Encoding).
  - **Predictive Core:** Linear Regression producing instant estimates in ₹ (INR).
  - **Delivery:** Browser-based Streamlit application deployed via Docker on Google Cloud Run.
  - **Output:** Clean metric card showing estimated annual compensation with academic disclaimer.
- **Suggested Visual:** High-level input-process-output flowchart diagram.

---

### Slide 5: System & Cloud Architecture
- **Slide Title:** System Architecture & Cloud Topology
- **Key Bullet Points:**
  - 3-tier architecture: Client Browser $\rightarrow$ Cloud Run Ingress $\rightarrow$ Docker Container.
  - Google Cloud Run automatically manages HTTPS termination and request routing.
  - Zero-maintenance serverless execution with instant scale-to-zero capabilities.
  - In-memory deserialization of `salary_model.pkl` via Joblib for sub-second inference.
- **Suggested Visual:** Figure 1 Architecture Diagram from report (Mermaid diagram).

---

### Slide 6: Technologies & Tool Stack
- **Slide Title:** Technology Stack
- **Key Bullet Points:**
  - **Language:** Python 3.12 (core programming).
  - **Data Libraries:** Pandas (tabular manipulation) & NumPy (numerical arrays).
  - **Machine Learning:** Scikit-learn (Pipeline, OneHotEncoder, Linear Regression).
  - **Model Persistence:** Joblib (`salary_model.pkl`).
  - **Web Framework:** Streamlit (clean Python-native data UI).
  - **DevOps & Cloud:** Docker (containerization) & Google Cloud Run (serverless hosting).
- **Suggested Visual:** 2x3 grid displaying logos of Python, Scikit-learn, Streamlit, Docker, and GCP.

---

### Slide 7: Dataset & Preprocessing Pipeline
- **Slide Title:** Dataset & Feature Preprocessing
- **Key Bullet Points:**
  - **Dataset Size:** 600 records (80% train / 20% test split).
  - **Numerical Features:** `age`, `years_experience`, `weekly_hours` (passthrough).
  - **Categorical Features:** `education_level` (3 categories), `job_level` (4 categories).
  - **Encoding Strategy:** `OneHotEncoder(drop='first')` prevents dummy variable trap.
  - **Transparency:** Clearly documented as synthetic educational data generated with statistical noise.
- **Suggested Visual:** Dataset preview table snapshot (Table 4 from report).

---

### Slide 8: Model Evaluation & Performance Metrics
- **Slide Title:** Model Training & Genuine Evaluation Metrics
- **Key Bullet Points:**
  - **Algorithm:** Supervised Multiple Linear Regression.
  - **Mean Absolute Error (MAE):** ₹47,097.10 (average deviation < ₹48k).
  - **Root Mean Squared Error (RMSE):** ₹60,747.94.
  - **R-squared ($R^2$ Score):** 0.9870 (98.7% variance explained).
  - High $R^2$ reflects the underlying synthetic linear relationship designed for clear viva demonstration.
- **Suggested Visual:** Actual vs. Predicted scatter plot (Figure 4 from report).

---

### Slide 9: Cloud Deployment & Containerization
- **Slide Title:** Cloud Deployment Strategy
- **Key Bullet Points:**
  - **Docker Base Image:** `python:3.12-slim` (lightweight, minimal attack surface).
  - **Dynamic Port Binding:** Maps `$PORT` environment variable (default 8080) for Cloud Run.
  - **Serverless Autoscaling:** Scales dynamically from 0 to N instances on demand.
  - **Cost Efficiency:** Pay-as-you-use billing guarantees zero cost when idle.
  - **Global Access:** Public HTTPS URL accessible from desktop, tablet, and mobile devices.
- **Suggested Visual:** Dockerfile snippet + Cloud Run service architecture icon.

---

### Slide 10: Testing Results & Sample Predictions
- **Slide Title:** Testing Scenarios & Sample Outputs
- **Key Bullet Points:**
  - **TC1 (Normal Mid):** 30 yrs, 5 exp, Masters, Mid $\rightarrow$ **₹9,96,300**
  - **TC2 (Fresh Entry):** 22 yrs, 0 exp, Bachelors, Junior $\rightarrow$ **₹2,61,146**
  - **TC3 (Senior Veteran):** 50 yrs, 25 exp, Masters, Senior $\rightarrow$ **₹25,60,662**
  - **TC4 (Managerial):** 30 yrs, 5 exp, Masters, Manager $\rightarrow$ **₹16,40,358**
  - All test cases verified against saved model with 100% execution pass rate.
- **Suggested Visual:** Screenshot of Streamlit output card (Figure 7).

---

### Slide 11: Advantages & Cloud Concepts Applied
- **Slide Title:** Advantages of Cloud-Hosted AI
- **Key Bullet Points:**
  - **On-Demand Resource Provisioning:** Instant resource allocation without physical hardware setup.
  - **Elasticity:** Automated horizontal scaling based on live user traffic.
  - **Remote Collaboration:** Centralized model updates instantly propagate to all users globally.
  - **Maintainability:** Containerization eliminates the *"works on my machine"* problem.
- **Suggested Visual:** Cloud benefit icons (Scalability, Security, Global Accessibility, Cost Savings).

---

### Slide 12: Limitations, Future Scope & Conclusion
- **Slide Title:** Conclusion & Future Roadmap
- **Key Bullet Points:**
  - **Achievements:** Successfully trained and deployed an explainable AI salary predictor on Google Cloud Run.
  - **Current Limitations:** Synthetic dataset, strictly linear relationships, educational scope.
  - **Future Scope:** Implement Random Forest / XGBoost, integrate Firestore database, add Explainable AI (SHAP).
  - **Summary:** Demonstrates the seamless integration of Machine Learning and Cloud Computing in an engineering project.
- **Suggested Visual:** Thank You text + Q&A invitation block.
