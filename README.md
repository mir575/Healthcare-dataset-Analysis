**Healthcare Dataset Analysis**

**Project Overview**

This project involves the analysis of a healthcare dataset containing patient information, medical conditions, and test results. The primary focus of this project was to clean the dataset, explore it using data visualizations, and then prepare it for predictive analysis using machine learning models.

![Power BI Desktop 9_8_2024 11_16_07 PM](https://github.com/user-attachments/assets/daa22711-1566-482b-9411-8de52c04f333)

![Power BI Desktop 9_8_2024 11_16_26 PM](https://github.com/user-attachments/assets/1a0e4447-2660-400a-89ca-6d7816c6cf1e)


**Dataset Information**

The dataset contains information on patient demographics, medical conditions, insurance details, and test results. The goal of the analysis is to gain insights into the data and, potentially, predict test results (Normal, Abnormal, Inconclusive).

**Key Columns in the Dataset:**

Name: The name of the patient (not used for analysis).

Age: The age of the patient.

Gender: Gender of the patient.

Blood Type: Patient's blood group (e.g., A+, O-, etc.).

Medical Condition: Medical condition(s) diagnosed (e.g., Diabetes, Hypertension).

Billing Amount: The amount billed for treatment.

Admission Type: Type of admission (Emergency, Urgent, Elective).

Test Results: The results of medical tests, which could be Normal, Abnormal, or Inconclusive.

**Tools Used**

Python: Used for initial data cleaning and preprocessing.

Pandas: For handling dataframes and cleaning.

Power BI: For data visualization and generating insights.

**Data Cleaning:**
Several steps were undertaken to clean the dataset and prepare it for analysis:

1) Standardization of Text: Columns like Name, Gender, Blood Type, and Medical Condition were standardized to a consistent format (e.g., title case).

2) Handling Missing Values: Missing values were addressed, either through removal or imputation with median values for numeric fields.

3) Removing Duplicates: Duplicate rows, particularly in patient records, were removed to ensure data integrity.

4) Label Encoding and One-Hot Encoding: Categorical columns such as Gender, Medical Condition, and Test Results were converted to numerical format to prepare for machine learning tasks.


