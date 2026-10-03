import joblib, numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data/employee_salary_data.csv")
print("Rows:", len(df), "| Missing values:", int(df.isnull().sum().sum()))
X, y = df.drop(columns="salary"), df["salary"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
pre = ColumnTransformer([("cat", OneHotEncoder(drop="first"), ["education_level", "job_level"])],
                        remainder="passthrough")
model = Pipeline([("prep", pre), ("reg", LinearRegression())]).fit(Xtr, ytr)
p = model.predict(Xte)
mse = mean_squared_error(yte, p)
print(f"Train size: {len(Xtr)} | Test size: {len(Xte)}")
print(f"MAE : {mean_absolute_error(yte, p):,.2f}\nMSE : {mse:,.2f}\nRMSE: {np.sqrt(mse):,.2f}\nR2  : {r2_score(yte, p):.4f}")
joblib.dump(model, "model/salary_model.pkl")
print("Model saved to model/salary_model.pkl")
