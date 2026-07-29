# Phase 16 – Power BI Dashboard Report

## Project Title

**Smart Crop Yield Prediction & Agricultural Decision Support System**

---

# Phase Objective

The objective of Phase 16 is to design and develop an interactive **Power BI Dashboard** that provides meaningful insights into agricultural production, crop yield, weather conditions, soil health, and machine learning prediction results.

Unlike the Streamlit application, which is used for making crop yield predictions, the Power BI dashboard focuses on **data visualization, business intelligence, and decision support** for farmers, government agencies, agricultural organizations, researchers, and policy makers.

---

# Dashboard Overview

The dashboard was built using **Microsoft Power BI Desktop** and consists of five interactive report pages:

1. Executive Dashboard
2. Crop Analysis
3. Weather Analysis
4. Soil Analysis
5. Prediction Analysis

Each page is designed to answer specific agricultural business questions using interactive charts, KPIs, filters, and drill-through functionality.

---

# Dataset Used

The dashboard uses the processed agricultural dataset generated during previous project phases.

Dataset:

```
data/processed/final_dataset.csv
```

The dataset contains historical crop production records along with engineered features created during Feature Engineering.

Main attributes include:

- State
- Crop
- Season
- Year
- Area
- Production
- Yield
- Annual Rainfall
- Total Rainfall
- Average Temperature
- Average Humidity
- Soil pH
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Fertilizer
- Pesticide

The Prediction Analysis page additionally uses:

```
predictions.csv
```

which contains:

- Actual Yield
- Predicted Yield
- Prediction Error

---

# Data Preparation

The dataset was imported into Power BI using:

```
Home
→ Get Data
→ Text / CSV
```

Power Query Editor was used for preprocessing before visualization.

The following validation steps were performed:

- Verified data types
- Removed blank rows
- Removed duplicate records
- Renamed columns where required
- Checked missing values
- Verified numerical columns
- Verified categorical columns

The cleaned dataset was then loaded into Power BI.

---

# Data Model

The dashboard primarily uses a **single-table data model**.

Therefore:

- No table relationships are required for the main dashboard.

For Prediction Analysis, a dedicated prediction dataset containing both actual and predicted values was used.

---

# DAX Measures

The following DAX measures were created.

## Total Production

```DAX
Total Production =
SUM(final_df[Production])
```

---

## Average Yield

```DAX
Average Yield =
AVERAGE(final_df[Yield])
```

---

## Total Area

```DAX
Total Area =
SUM(final_df[Area])
```

---

## Total Crops

```DAX
Total Crops =
DISTINCTCOUNT(final_df[Crop])
```

---

## Total States

```DAX
Total States =
DISTINCTCOUNT(final_df[State])
```

---

## Average Rainfall

```DAX
Average Rainfall =
AVERAGE(final_df[Annual_Rainfall])
```

---

# Dashboard Pages

---

# Page 1 – Executive Dashboard

## Purpose

Provides a high-level overview of agricultural production and crop performance.

### KPI Cards

- Total Production
- Average Yield
- Total States
- Total Crops
- Average Rainfall

### Visualizations

- Yield by State (Clustered Bar Chart)
- Production Trend by Year (Line Chart)
- Crop Distribution (Donut Chart)

### Slicers

- State
- Crop
- Year
- Season

### Business Insights

This page helps users quickly understand:

- Overall crop production
- Average crop yield
- Number of cultivated crops
- State-wise agricultural performance
- Historical production trends

---

# Page 2 – Crop Analysis

## Purpose

Provides detailed crop performance analysis.

### Visualizations

- Top 10 Crops by Yield
- Crop-wise Production
- Area vs Yield (Scatter Plot)
- Seasonal Crop Distribution

### Business Questions Answered

- Which crop has the highest yield?
- Which crop occupies the largest cultivated area?
- Which season provides the highest production?
- Which crops contribute the most to total production?

---

# Page 3 – Weather Analysis

## Purpose

Analyzes the effect of weather conditions on agricultural yield.

### Visualizations

- Rainfall vs Yield
- Temperature vs Yield
- Humidity vs Yield
- Weather Trend by Year

### Business Questions Answered

- Does rainfall improve crop yield?
- Which temperature range is most suitable?
- How does humidity influence production?
- Which weather conditions produce better agricultural output?

---

# Page 4 – Soil Analysis

## Purpose

Evaluates soil quality and nutrient distribution across states.

### Visualizations

- Nitrogen Distribution
- Phosphorus Distribution
- Potassium Distribution
- Soil pH by State

### Business Questions Answered

- Which states have nutrient-rich soil?
- Which nutrients influence crop yield the most?
- How does soil pH vary across regions?
- Which states require soil improvement?

---

# Page 5 – Prediction Analysis

## Purpose

Compares machine learning predictions with actual crop yield.

The prediction dataset contains:

- Actual Yield
- Predicted Yield
- Prediction Error

### Visualizations

- Actual Yield vs Predicted Yield
- Prediction Error by Crop
- Prediction Error by State
- RMSE KPI Card
- R² Score KPI Card
- Feature Importance Image (generated using SHAP)

### Business Questions Answered

- How accurate is the prediction model?
- Which crops have the lowest prediction error?
- Which states produce the most accurate predictions?
- Which features have the greatest influence on crop yield?

---

# Interactive Features

The dashboard provides multiple interactive capabilities.

## Global Filters

Users can filter the dashboard using:

- State
- Crop
- Season
- Year

All report pages respond dynamically to the selected filters.

---

# Drill-through

Drill-through functionality was implemented to enable users to navigate from:

```
State
        ↓
Crop Details
```

Users can right-click a state and explore detailed crop information for that specific region.

---

# Tooltips

Custom tooltips display additional information when hovering over visuals.

Displayed information includes:

- Crop Name
- State
- Yield
- Production
- Rainfall
- Soil pH

This improves the dashboard's usability without overcrowding the visuals.

---

# Dashboard Theme

A professional agricultural theme was applied.

### Color Palette

- Green
- Brown
- White

These colors were selected to represent:

- Agriculture
- Soil
- Crops
- Nature

Professional fonts, spacing, and consistent formatting were used throughout the report.

---

# Validation

The completed dashboard was validated using the following checklist.

✔ All visuals respond correctly to slicers

✔ KPI values match the source dataset

✔ DAX measures return correct results

✔ No blank or broken visuals

✔ Drill-through works correctly

✔ Tooltips display correct information

✔ Dashboard performance is smooth

✔ Prediction analysis matches machine learning output

---

# Dashboard Deliverables

```
powerbi/
│
├── Crop_Yield_Dashboard.pbix
├── Crop_Yield_Dashboard.pdf
│
├── dashboard_screenshots/
│   ├── Executive_Dashboard.png
│   ├── Crop_Analysis.png
│   ├── Weather_Analysis.png
│   ├── Soil_Analysis.png
│   └── Prediction_Analysis.png
```

---

# Technologies Used

- Microsoft Power BI Desktop
- DAX
- Power Query
- CSV Dataset
- Machine Learning Prediction Output
- SHAP Feature Importance

---

# Key Outcomes

The dashboard successfully transforms historical agricultural data and machine learning predictions into an interactive decision-support system.

It enables users to:

- Analyze crop production trends.
- Compare crop yield across states.
- Study the impact of weather conditions.
- Evaluate soil nutrient distribution.
- Monitor machine learning prediction accuracy.
- Explore agricultural insights using interactive visualizations.

The dashboard complements the Streamlit prediction application by focusing on business intelligence, reporting, and analytical decision-making.

---

# Conclusion

Phase 16 completes the Business Intelligence layer of the Smart Crop Yield Prediction & Agricultural Decision Support System.

Using Microsoft Power BI, an interactive dashboard was developed to visualize agricultural production, crop performance, weather trends, soil characteristics, and prediction results. Through KPIs, charts, slicers, drill-through, and tooltips, the dashboard provides stakeholders with actionable insights for data-driven agricultural planning.

Together with the Streamlit prediction application and the machine learning model, the Power BI dashboard forms the final component of the end-to-end agricultural analytics solution.