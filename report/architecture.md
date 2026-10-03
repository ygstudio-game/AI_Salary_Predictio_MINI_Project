# Cloud Architecture & Data Flow Specification

This document details the system, application, and machine learning architecture for the **AI-Based Employee Salary Prediction System Using Cloud Computing**.

---

## 1. System Architecture Overview

The application adopts a 3-tier cloud-native design:
1. **Client Tier:** Web browser interacting with the Streamlit frontend.
2. **Serverless Application Tier:** Containerized Python runtime executing Streamlit on Google Cloud Run.
3. **Machine Learning Model Tier:** Serialized Scikit-learn Pipeline loaded in-memory.

```mermaid
graph TD
    A[End User / Web Browser] -->|HTTPS Request| B[GCP Cloud Run Ingress / Load Balancer]
    B --> C[Serverless Docker Container Instance]
    subgraph "Docker Container (Python 3.12-slim)"
        C --> D[Streamlit Server : Port 8080]
        D --> E[User Input Validation (Pandas DataFrame)]
        E --> F[Scikit-learn Pipeline]
        subgraph "ML Pipeline (salary_model.pkl)"
            F --> G[ColumnTransformer - OneHotEncoder]
            G --> H[Multiple Linear Regression Model]
        end
        H --> I[Predicted Salary Value in INR]
    end
    I -->|HTTPS Response| D
    D -->|Render Result Card| A
```

---

## 2. Machine Learning Workflow Architecture

The end-to-end machine learning lifecycle consists of 5 distinct stages:

```mermaid
flowchart LR
    subgraph "Stage 1: Data Preparation"
        A1[Generate Synthetic Data] --> A2[employee_salary_data.csv (600 rows)]
        A2 --> A3[Feature Selection & Cleaning]
    end

    subgraph "Stage 2: Model Training"
        A3 --> B1[80/20 Train-Test Split]
        B1 --> B2[ColumnTransformer Pipeline]
        B2 --> B3[Linear Regression Fitting]
        B3 --> B4[Evaluate Metrics: MAE, RMSE, R²]
    end

    subgraph "Stage 3: Serialization"
        B4 --> C1[Joblib Serializer]
        C1 --> C2[salary_model.pkl]
    end

    subgraph "Stage 4: Cloud Deployment"
        C2 --> D1[Package in Dockerfile]
        D1 --> D2[Build Container Image]
        D2 --> D3[Deploy to Google Cloud Run]
    end

    subgraph "Stage 5: Live Inference"
        D3 --> E1[Streamlit UI User Inputs]
        E1 --> E2[In-Memory Model Scoring]
        E2 --> E3[Display Predicted Salary in ₹]
    end
```

---

## 3. Detailed Component Breakdown

### 3.1 Client Tier
- Users access the application via any modern web browser across desktop, laptop, or mobile devices.
- Requests are encrypted over standard TLS/HTTPS.
- The interface provides validation rules (e.g., minimum age of 21, working hours between 35 and 55) to prevent out-of-bound inputs.

### 3.2 Cloud Run Serverless Ingress
- Google Cloud Run provisions a managed HTTPS ingress endpoint.
- Provides automatic TLS termination, DDoS mitigation, and request routing.
- **Autoscaling:** When request volume surges, Cloud Run instantiates additional container replicas. When traffic ceases, it scales down to zero, ensuring zero operational compute costs.

### 3.3 Application Container (Docker)
- Base Image: `python:3.12-slim` (minimal attack surface, under 200MB compressed).
- Port Binding: Reads dynamic `$PORT` environment variable (defaults to 8080).
- Headless execution: `streamlit run app.py --server.port=${PORT:-8080} --server.address=0.0.0.0 --server.headless=true`.

### 3.4 In-Memory Inference Pipeline
- Upon container cold start, `joblib.load("model/salary_model.pkl")` deserializes the Scikit-learn Pipeline into RAM.
- Incoming input dictionary is converted into a 1-row Pandas DataFrame.
- Categorical features (`education_level`, `job_level`) are dynamically transformed into indicator vectors.
- Regression coefficients compute the continuous salary prediction in sub-millisecond latency:
  $$\hat{y} = \max(0, \mathbf{w}^T \mathbf{x} + b)$$

---

## 4. Key Cloud Concepts Demonstrated

| Concept | Implementation in this Project |
| :--- | :--- |
| **On-Demand Provisioning** | Container instances launch immediately upon user HTTP request. |
| **Containers (Docker)** | Decouples code from underlying host OS, guaranteeing reproducibility. |
| **Serverless Architecture** | No OS patching, VM maintenance, or hardware management required. |
| **Elastic Scalability** | Automatically scales between 0 and N instances based on concurrent traffic. |
| **Remote Accessibility** | Accessible anywhere globally over standard internet protocols. |
| **Pay-As-You-Use** | Billing is calculated per millisecond of CPU/Memory consumption during active inference. |
