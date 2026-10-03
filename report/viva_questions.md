# Viva Voce Preparation Guide (35 Questions & Concise Answers)

This guide provides 35 concise, high-yield questions and answers designed specifically for the oral viva examination of the **AI-Based Employee Salary Prediction System Using Cloud Computing**.

---

### Machine Learning & Data Science Fundamentals

#### 1. What is Artificial Intelligence (AI)?
**Answer:** AI is the branch of computer science dedicated to creating software and systems capable of performing tasks that typically require human intelligence, such as reasoning, pattern recognition, and decision making.

#### 2. What is Machine Learning (ML)?
**Answer:** Machine Learning is a subset of AI that enables systems to automatically learn patterns from data and improve their performance on a specific task without being explicitly programmed.

#### 3. What is Supervised Learning?
**Answer:** Supervised learning is an ML paradigm where the model is trained on labeled data consisting of input features and the corresponding ground truth target outputs.

#### 4. What is Regression?
**Answer:** Regression is a supervised learning task used to predict a continuous numerical value (such as salary, price, or temperature) based on one or more independent variables.

#### 5. Why did you choose Linear Regression for this project?
**Answer:** Linear Regression is computationally lightweight, fast to train, highly explainable during viva, and provides clear mathematical relationships between employee attributes and compensation.

#### 6. What is the mathematical equation of Multiple Linear Regression?
**Answer:**
$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$
Where $\beta_0$ is the intercept, $\beta_i$ are feature coefficients, $x_i$ are input features, and $\epsilon$ is the error term.

#### 7. What is the target variable in your project?
**Answer:** The target variable is `salary` (the predicted annual compensation in Indian Rupees ₹).

#### 8. What are the features used in your model?
**Answer:** There are 5 features:
1. `age` (numerical)
2. `years_experience` (numerical)
3. `education_level` (categorical)
4. `job_level` (categorical)
5. `weekly_hours` (numerical)

#### 9. What is training data and testing data?
**Answer:**
- **Training Data:** The subset of records (80% / 480 rows) used by the algorithm to fit its weights.
- **Testing Data:** The unseen held-out subset (20% / 120 rows) used strictly to evaluate model accuracy.

#### 10. Why do we perform a train-test split?
**Answer:** To assess how well the model generalizes to completely new, unseen data and prevent overfitting on training records.

#### 11. What is One-Hot Encoding and why did you use `drop='first'`?
**Answer:** One-Hot Encoding converts categorical text values into binary indicator columns ($0$ or $1$). We drop the first category (`drop='first'`) to prevent multicollinearity (the "dummy variable trap").

#### 12. What is a Scikit-learn Pipeline?
**Answer:** A Pipeline chains data preprocessing (`ColumnTransformer`) and the estimator (`LinearRegression`) together into a single object, preventing data leakage and ensuring identical preprocessing at inference.

---

### Model Evaluation & Metrics

#### 13. What is Mean Absolute Error (MAE)?
**Answer:** MAE is the average magnitude of absolute differences between actual and predicted values:
$$\text{MAE} = \frac{1}{n} \sum |y_i - \hat{y}_i|$$
In our project, MAE is **₹47,097.10**.

#### 14. What is Root Mean Squared Error (RMSE)?
**Answer:** RMSE is the square root of the average squared errors:
$$\text{RMSE} = \sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$$
It penalizes larger deviations more heavily. Our RMSE is **₹60,747.94**.

#### 15. What is the $R^2$ Score (Coefficient of Determination)?
**Answer:** $R^2$ indicates the proportion of variance in the target variable that is explained by the input features. Our $R^2$ is **0.9870 (98.7%)**.

#### 16. Why is your $R^2$ score so high?
**Answer:** Because the model is trained on a synthetic educational dataset designed with consistent linear relationships between experience, designation, and salary, plus controlled noise.

---

### Python & Library Choices

#### 17. Why use Pandas?
**Answer:** Pandas provides efficient data structures (DataFrames) for importing CSV files, handling tabular structures, and preprocessing features.

#### 18. Why use NumPy?
**Answer:** NumPy provides optimized C-based numerical arrays and vector math needed for metric calculations (such as RMSE square roots).

#### 19. Why use Scikit-learn?
**Answer:** Scikit-learn is the standard Python machine learning library, offering tested implementations of Linear Regression, ColumnTransformer, and evaluation metrics.

#### 20. Why use Streamlit instead of Flask or Django?
**Answer:** Streamlit lets developers build clean, reactive data web applications purely in Python without writing HTML, CSS, or JavaScript, accelerating deployment.

#### 21. What is Joblib and why use it over Pickle?
**Answer:** Joblib is a Python library optimized for serializing large NumPy arrays and Scikit-learn pipelines to disk (`salary_model.pkl`) faster than standard pickle.

---

### Cloud Computing & Deployment Concepts

#### 22. What is Cloud Computing?
**Answer:** Cloud computing is the on-demand delivery of computing resources (servers, storage, databases, networking, and software) over the Internet with pay-as-you-go pricing.

#### 23. What are IaaS, PaaS, and SaaS?
**Answer:**
- **IaaS (Infrastructure as a Service):** Provides raw virtual machines and storage (e.g., Google Compute Engine, AWS EC2).
- **PaaS (Platform as a Service):** Provides runtime environments for deploying code without managing OS/servers (e.g., Google App Engine).
- **SaaS (Software as a Service):** Fully delivered end-user software over the web (e.g., Google Workspace, Gmail).

#### 24. What is Google Cloud Run and which model does it belong to?
**Answer:** Cloud Run is a fully managed **serverless container platform** (often classified under PaaS / Container-as-a-Service) that automatically runs and scales containerized applications.

#### 25. What is a Docker Container?
**Answer:** A container is a lightweight, standalone, executable package that bundles application code, libraries, runtime, and configuration together, ensuring identical execution across all platforms.

#### 26. What is the difference between a Virtual Machine and a Container?
**Answer:**
- **VMs** include a full guest Operating System and run on a hypervisor (heavy, slow boot).
- **Containers** share the host OS kernel and isolate at the process level (lightweight, rapid startup in seconds).

#### 27. What is Scalability in Cloud Computing?
**Answer:** Scalability is the capacity of a system to handle increasing load by adding resources (vertically by adding CPU/RAM, or horizontally by adding instances).

#### 28. What is Elasticity?
**Answer:** Elasticity is the ability of a cloud system to automatically expand or shrink resources dynamically in real-time according to fluctuating demand.

#### 29. What is "Scale-to-Zero"?
**Answer:** A key feature of serverless platforms like Cloud Run where active compute instances drop to 0 when there is no traffic, ensuring no costs are incurred during idle periods.

#### 30. What is Remote Accessibility?
**Answer:** The capability of an application deployed on the cloud to be securely accessed from any web browser or device worldwide over HTTPS.

#### 31. What is the Pay-as-You-Use pricing model?
**Answer:** You only pay for the exact resources (vCPU seconds, memory GB-seconds, and HTTP requests) consumed while handling queries, rather than paying 24/7 for an idle server.

---

### Project-Specific In-Depth Viva Questions

#### 32. Can you explain your end-to-end architecture?
**Answer:** The user enters 5 attributes in the Streamlit UI. The browser sends an HTTPS request to Google Cloud Run, which routes it into a Docker container. The Streamlit script passes the inputs into the Scikit-learn Pipeline (`salary_model.pkl`), which encodes categorical variables and predicts salary in INR using Linear Regression.

#### 33. What are the key limitations of your project?
**Answer:**
1. Trained on synthetic data rather than proprietary corporate payroll records.
2. Does not account for geographical living costs, company size, or stock options.
3. Linear models cannot capture complex non-linear compensation tiers.

#### 34. What is the Future Scope for this project?
**Answer:**
1. Upgrading to ensemble algorithms like Random Forest or XGBoost.
2. Integrating a cloud database (Google Firestore) for logging predictions.
3. Adding Explainable AI (SHAP/LIME) to show which factors impacted the salary most.

#### 35. Why shouldn't this system be used for real HR hiring decisions?
**Answer:** Because real compensation depends on market conditions, company budgets, and candidate negotiation; an educational model trained on simplified synthetic data is strictly a demonstration prototype.
