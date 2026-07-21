# Data Cleaning Report

## Project Information

| Item | Details |
|------|---------|
| Project Name | Smart Crop Yield Prediction & Agricultural Decision Support System |
| Phase | Phase 5 – Data Cleaning |
| Prepared By | Pawan Bhardwaj |
| Version | 1.0 |
| Status | Completed |

---

# Objective

The objective of this phase is to improve data quality by handling missing values, removing duplicate records, correcting data types, standardizing categorical values, and preparing clean datasets for exploratory data analysis and machine learning.

---

# Datasets Used

- Crop Yield Dataset
- Weather Dataset
- Soil Dataset

---

# Data Cleaning Tasks Performed

## 1. Missing Value Handling

Missing values were checked using:

```python
df.isnull().sum()
```

Observation:

- Missing values were handled only where necessary.
- Numerical columns were imputed using median values when appropriate.
- Categorical columns were filled using the most frequent value or "Unknown" if required.

---

## 2. Duplicate Record Removal

Duplicate rows were identified using:

```python
df.duplicated().sum()
```

Observation:

- Duplicate records were removed where present.
- The final cleaned datasets contain only unique records.

---

## 3. Data Type Verification

Data types were validated using:

```python
df.info()
```

Observation:

- Numerical features use numeric data types.
- Categorical features use string/object data types.

---

## 4. Text Standardization

Categorical columns were standardized by:

- Removing leading and trailing spaces.
- Applying consistent capitalization.
- Ensuring consistent naming for states, crops, and seasons.

---

## 5. Invalid Value Handling

The following validations were performed:

- Negative Area values
- Negative Production values
- Negative Yield values
- Invalid year values

Any invalid records were corrected or removed if necessary.

---

## 6. Clean Dataset Creation

The cleaned datasets were exported to:

```text
data/processed/
├── crop_yield_cleaned.csv
├── weather_cleaned.csv
└── soil_cleaned.csv
```

---

# Cleaning Summary

| Task | Status |
|------|--------|
| Missing Values | ✅ Completed |
| Duplicate Removal | ✅ Completed |
| Data Type Validation | ✅ Completed |
| Text Standardization | ✅ Completed |
| Invalid Value Handling | ✅ Completed |
| Clean Dataset Export | ✅ Completed |

---

# Deliverables

- Clean Crop Dataset
- Clean Weather Dataset
- Clean Soil Dataset
- Data Cleaning Notebook
- Data Cleaning Report

---

# Conclusion

The datasets have been successfully cleaned and standardized. The cleaned datasets are now ready for dataset integration and exploratory data analysis.

---

## Next Phase

Phase 6 – Dataset Merging

---

Prepared By:

Pawan Bhardwaj