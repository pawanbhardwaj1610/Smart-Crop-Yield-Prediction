# Dataset Merging Report

## Project Information

| Item | Details |
|------|---------|
| **Project Name** | Smart Crop Yield Prediction & Agricultural Decision Support System |
| **Phase** | Phase 6 – Dataset Merging |
| **Prepared By** | Pawan Bhardwaj |
| **Version** | 1.0 |
| **Status** | Completed |
| **Date** | *(Add Current Date)* |

---

# Objective

The objective of this phase is to integrate multiple datasets into a single analytical dataset that contains agricultural production, weather conditions, and soil characteristics. A unified dataset is essential for performing Exploratory Data Analysis (EDA), Feature Engineering, and Machine Learning model development.

The merged dataset enables the project to analyze the combined impact of climatic conditions and soil nutrients on crop yield prediction.

---

# Background

The project uses data collected from multiple independent sources. Since each dataset contains different aspects of agricultural information, they must be merged using common identifiers.

The datasets include:

- Historical Crop Production Data
- State-wise Weather Data
- State-wise Soil Data

These datasets individually cannot provide sufficient information for predictive modeling. Combining them creates a comprehensive dataset suitable for advanced analytics.

---

# Datasets Used

## 1. Crop Yield Dataset

Contains historical agricultural information including:

- State
- Crop
- Crop Year
- Season
- Area
- Production
- Annual Rainfall
- Fertilizer
- Pesticide
- Yield

Location:

```text
data/processed/crop_yield_cleaned.csv
```

---

## 2. Weather Dataset

Contains historical weather information including:

- State
- Year
- Average Temperature
- Total Rainfall
- Average Humidity

Location:

```text
data/processed/weather_cleaned.csv
```

---

## 3. Soil Dataset

Contains soil nutrient information including:

- State
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- pH Value

Location:

```text
data/processed/soil_cleaned.csv
```

---

# Merge Strategy

The integration process was completed in two stages.

## Stage 1

Crop Dataset + Weather Dataset

### Merge Keys

- State
- Year

### Join Type

```python
Left Join
```

Reason:

The Crop Yield dataset serves as the primary dataset. Every crop record should be retained even if weather information is unavailable for some observations.

---

## Stage 2

Merged Dataset + Soil Dataset

### Merge Key

- State

### Join Type

```python
Left Join
```

Reason:

Soil information is available at the state level and is joined to every crop record belonging to that state.

---

# Data Preparation Before Merging

Before merging the datasets, several preprocessing steps were performed to ensure consistency.

## State Name Standardization

State names were standardized across all datasets.

Examples include:

| Original | Updated |
|----------|----------|
| Jammu And Kashmir | Jammu and Kashmir |
| Orissa | Odisha |
| Uttaranchal | Uttarakhand |
| Pondicherry | Puducherry |

This step prevented merge failures caused by inconsistent naming conventions.

---

## Column Name Standardization

Column names were reviewed to ensure consistency.

Examples:

- Crop_Year → Year
- State → State

---

## Data Type Validation

Merge key columns were verified to ensure matching data types.

For example:

```python
State → object
Year → int64
```

Matching data types are required for successful joins.

---

# Merge Implementation

The datasets were merged using the Pandas `merge()` function.

Example:

```python
crop_weather = pd.merge(
    crop_df,
    weather_df,
    on=["State", "Year"],
    how="left"
)

final_df = pd.merge(
    crop_weather,
    soil_df,
    on="State",
    how="left"
)
```

---

# Validation Performed

After merging, the following validation checks were completed.

## Dataset Shape

Verified:

```python
final_df.shape
```

Purpose:

- Confirm expected number of rows
- Verify new columns were added successfully

---

## Missing Values

Checked using:

```python
final_df.isnull().sum()
```

Observation:

Some missing values were identified in weather and soil attributes due to unmatched records during merging.

Example:

- avg_temp_C
- total_rainfall_mm
- avg_humidity_percent
- N
- P
- K
- pH

The primary reason was inconsistent state names or missing records in the source datasets.

State names were standardized and the merge process was repeated to minimize missing values.

---

## Duplicate Records

Checked using:

```python
final_df.duplicated().sum()
```

Purpose:

Ensure dataset merging did not introduce duplicate observations.

---

## Data Integrity

Verified that:

- All crop records were retained.
- Weather information aligned correctly with each state and year.
- Soil information aligned correctly with each state.

---

# Challenges Encountered

Several challenges were identified during dataset integration.

## Challenge 1

Inconsistent State Names

Examples:

- Jammu And Kashmir
- Jammu and Kashmir

Solution:

State names were standardized using dictionary mapping before merging.

---

## Challenge 2

Missing Matches

Some crop records did not find matching weather or soil records.

Solution:

- Verified merge keys.
- Standardized state names.
- Repeated merge process.
- Remaining missing values were documented for later preprocessing.

---

## Challenge 3

Column Consistency

Some datasets used different naming conventions.

Solution:

Column names were standardized before merging.

---

# Final Dataset

The merged dataset contains information from all three datasets.

Included Features:

- Crop Information
- Weather Information
- Soil Nutrients
- Rainfall
- Fertilizer Usage
- Pesticide Usage
- Yield

This dataset serves as the master dataset for all remaining phases of the project.

---

# Deliverables

Completed deliverables include:

- Crop Dataset Integration
- Weather Dataset Integration
- Soil Dataset Integration
- State Name Standardization
- Merge Validation
- Final Analytical Dataset

Generated Files:

```text
data/processed/final_dataset.csv
```

Notebook:

```text
notebooks/04_Data_Merging.ipynb
```

Report:

```text
reports/06_Data_Merging_Report.md
```

---

# Key Outcomes

✔ Successfully merged three datasets.

✔ Standardized state names.

✔ Preserved all crop production records.

✔ Created a unified analytical dataset.

✔ Validated merged dataset for missing values and duplicates.

✔ Prepared the dataset for Exploratory Data Analysis (EDA).

---

# Conclusion

The Dataset Merging phase successfully integrated agricultural, weather, and soil datasets into a unified analytical dataset. Data consistency issues, including state name mismatches and column naming differences, were resolved prior to merging.

The resulting dataset provides a comprehensive view of agricultural production by combining environmental, climatic, and soil-related attributes. This integrated dataset forms the foundation for subsequent phases, including Exploratory Data Analysis (EDA), Feature Engineering, Machine Learning model development, and deployment.

---

# Next Phase

## Phase 7 – Exploratory Data Analysis (EDA)

Objectives:

- Understand feature distributions.
- Identify trends and patterns.
- Analyze relationships between variables.
- Detect outliers.
- Generate business insights.
- Support feature engineering and model selection.

---

**Prepared By**

**Pawan Bhardwaj**

**Project:** Smart Crop Yield Prediction & Agricultural Decision Support System

**GitHub Repository:** https://github.com/pawanbhardwaj1610/Smart-Crop-Yield-Prediction