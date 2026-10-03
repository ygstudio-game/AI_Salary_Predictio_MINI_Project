# Software & Model Testing Report

This document records the comprehensive testing methodology, functional verification, model validation, and boundary test cases conducted for the **AI-Based Employee Salary Prediction System Using Cloud Computing**.

---

## 1. Testing Objectives

1. **Functional Integrity:** Verify that Streamlit UI controls accurately capture and validate user input parameters.
2. **Model Precision:** Verify that the trained Scikit-learn Pipeline produces realistic, non-negative salary predictions across diverse employee profiles.
3. **Container Compatibility:** Verify that Docker container runs headlessly and binds properly to the assigned port.
4. **Boundary & Robustness:** Verify that edge inputs (e.g. 0 years experience or maximum age) execute without crashing.

---

## 2. Test Execution Matrix (Verified Genuine Model Outputs)

The following test cases were executed directly against the trained model (`salary_model.pkl`) using `test_results.txt`:

| Test ID | Test Scenario | Input Feature Vector | Expected Behavior | Actual Predicted Output | Result |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **TC-01** | **Normal Mid-Level Profile** | • Age: 30<br>• Experience: 5 yrs<br>• Education: Masters<br>• Job Level: Mid<br>• Weekly Hours: 40 | Predict realistic mid-career IT salary (~₹9L–₹11L) | **₹9,96,300** | **PASS** |
| **TC-02** | **Fresh Graduate / Entry Level** | • Age: 22<br>• Experience: 0 yrs<br>• Education: Bachelors<br>• Job Level: Junior<br>• Weekly Hours: 40 | Predict entry-level graduate salary (~₹2.5L–₹3.5L) | **₹2,61,146** | **PASS** |
| **TC-03** | **Senior Veteran Profile** | • Age: 50<br>• Experience: 25 yrs<br>• Education: Masters<br>• Job Level: Senior<br>• Weekly Hours: 45 | Substantially higher compensation reflecting 2.5 decades experience | **₹25,60,662** | **PASS** |
| **TC-04** | **Managerial Responsibility** | • Age: 30<br>• Experience: 5 yrs<br>• Education: Masters<br>• Job Level: Manager<br>• Weekly Hours: 40 | Predict premium for managerial designation compared to Mid level | **₹16,40,358** | **PASS** |
| **TC-05** | **Doctorate Degree Increment** | • Age: 30<br>• Experience: 5 yrs<br>• Education: PhD<br>• Job Level: Mid<br>• Weekly Hours: 40 | Predict educational increment over Masters degree profile | **₹11,03,917** | **PASS** |

---

## 3. Comparative Observations & Insights

1. **Experience Sensitivity:** Comparing TC-02 (0 yrs) and TC-03 (25 yrs), salary increases progressively by ~₹23 Lakhs, confirming that years of experience is the strongest continuous predictor.
2. **Designation Premium:** Comparing TC-01 (Mid) and TC-04 (Manager), keeping all other variables identical (Age 30, Exp 5, Masters, 40 hrs), shifting to Manager yields a **₹6,44,058** elevation, demonstrating strong categorical separation.
3. **Educational Uplift:** Comparing TC-01 (Masters) and TC-05 (PhD) under identical demographics, the doctorate qualification provides an increment of **₹1,07,617**.

---

## 4. Web UI & Functional Validation

| Check # | Component | Test Action | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **UI-01** | Number Input (`Age`) | Set minimum boundary (21) and maximum (60) | Widget restricts values to valid working age | Values strictly between 21 and 60 | **PASS** |
| **UI-02** | Slider (`Experience`) | Set minimum (0) and maximum (25) | Slider smoothly traverses discrete years | Exact integer values passed | **PASS** |
| **UI-03** | Selectbox (`Education`) | Choose between Bachelors, Masters, PhD | Selected string passed into DataFrame | Formats correctly for OneHotEncoder | **PASS** |
| **UI-04** | Selectbox (`Job Level`) | Choose Junior, Mid, Senior, Manager | Categorical mapping matches training categories | Matches categories without KeyError | **PASS** |
| **UI-05** | Predict Button | Click "Predict Salary" | Real-time computation and display of formatted INR card | Renders metric card with ₹ currency | **PASS** |
| **UI-06** | Disclaimer Note | Review bottom of screen | Display disclaimer on educational nature | Caption displayed legibly | **PASS** |

---

## 5. Non-Negative Guarantee Test
Because standard Linear Regression is an unbounded linear equation, edge cases could theoretically generate negative values for hypothetical zero-experience profiles. The application enforces a non-negative floor:
$$\text{Output} = \max(0, \hat{y})$$
This ensures that the displayed salary can never drop below zero.
