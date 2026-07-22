# Feature Engineering Report

## Project Information

| Item | Details |
|------|---------|
| **Project Name** | Smart Crop Yield Prediction & Agricultural Decision Support System |
| **Phase** | Phase 8 – Feature Engineering |
| **Prepared By** | Pawan Bhardwaj |
| **Version** | 1.0 |
| **Status** | Completed |
| **Date** | *(Add Current Date)* |

---

# Objective

The objective of this phase is to transform the merged agricultural dataset into a machine learning-ready dataset by selecting important features, creating new meaningful variables, encoding categorical data, and improving data quality.

Feature engineering helps the model better understand the relationship between crop characteristics, weather conditions, soil properties, and agricultural inputs for accurate crop yield prediction.

---

# Background

After completing the Dataset Merging phase, the project contained a unified dataset combining:

- Crop production information
- Weather conditions
- Soil characteristics

However, the raw merged dataset required further processing before applying machine learning algorithms.

The main challenges were:

- Categorical variables were in text format.
- Features had different numerical ranges.
- Some missing values were present.
- Additional agricultural indicators were required for better prediction.

Therefore, feature engineering was performed to prepare the final dataset.

---

# Input Dataset

The feature engineering process was performed on:

```text
data/processed/final_dataset.csv