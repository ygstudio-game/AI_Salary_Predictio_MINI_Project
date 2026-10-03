"""Creates a SYNTHETIC educational salary dataset (not real company data)."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
n = 600
exp = rng.integers(0, 26, n)
age = np.clip(21 + exp + rng.integers(0, 6, n), 21, 60)
edu = rng.choice(["Bachelors", "Masters", "PhD"], n, p=[0.55, 0.35, 0.10])
lvl = rng.choice(["Junior", "Mid", "Senior", "Manager"], n, p=[0.35, 0.30, 0.25, 0.10])
hours = rng.integers(35, 56, n)
salary = (250000 + 45000 * exp + 15000 * (age - 21)
          + pd.Series(edu).map({"Bachelors": 0, "Masters": 120000, "PhD": 250000}).values
          + pd.Series(lvl).map({"Junior": 0, "Mid": 250000, "Senior": 600000, "Manager": 900000}).values
          + 4000 * (hours - 40) + rng.normal(0, 60000, n))
pd.DataFrame(dict(age=age, years_experience=exp, education_level=edu, job_level=lvl,
                  weekly_hours=hours, salary=salary.round(-2).astype(int))).to_csv("data/employee_salary_data.csv", index=False)
