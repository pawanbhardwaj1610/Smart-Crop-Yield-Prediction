# Data Validation Report

## Project
Smart Crop Yield Prediction & Agricultural Decision Support System

---

## Objective

The objective of this phase is to validate the quality of the collected datasets before performing data cleaning and preprocessing. Data validation ensures that the datasets are complete, consistent, and suitable for machine learning.

---

# Datasets Used

| Dataset | Description |
|----------|-------------|
| Crop Yield Dataset | Historical crop production and yield information |
| Weather Dataset | State-wise weather data from 1997–2020 |
| Soil Dataset | State-wise soil characteristics |

---

# Validation Checks Performed

## 1. Missing Values

Missing values were checked using:

```python
df.isnull().sum()
```

### Result

- Crop Dataset: No missing values found.
- Weather Dataset: No missing values found.
- Soil Dataset: No missing values found.

---

## 2. Duplicate Records

Duplicate records were checked using:

```python
df.duplicated().sum()
```

### Result

- Crop Dataset: No duplicate records found.
- Weather Dataset: No duplicate records found.
- Soil Dataset: No duplicate records found.

---

## 3. Data Types

Data types were verified using:

```python
df.info()
```

### Result

- Numerical columns have appropriate numeric data types.
- Categorical columns have appropriate string/object data types.

---

## 4. Invalid Values

The following checks were performed:

- Negative Area values
- Negative Production values
- Negative Yield values
- Invalid Year values

### Result

No invalid values requiring immediate correction were identified.

---

## 5. Categorical Data Validation

The following categorical columns were reviewed:

- State
- Crop
- Season

### Result

Values appear consistent and suitable for further preprocessing.

---

# Validation Summary

| Validation Check | Status |
|------------------|--------|
| Missing Values | ✅ Passed |
| Duplicate Records | ✅ Passed |
| Data Types | ✅ Passed |
| Invalid Values | ✅ Passed |
| Categorical Values | ✅ Passed |

---

# Conclusion

The datasets successfully passed the initial validation process. They are suitable for the next phase of the project, which is **Data Cleaning**. Any additional preprocessing required during feature engineering will be addressed in later phases.

---

**Prepared By:** Pawan Bhardwaj

**Project:** Smart Crop Yield Prediction & Agricultural Decision Support System