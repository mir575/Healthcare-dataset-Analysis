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

**The original dataset contained about 55000 rows before cleaning. After Data Cleaning, The dataset now has 46236 rows.**

**Visualizations**

The following visualizations were created using Power BI to explore and present key insights from the dataset:

**Gender Distribution by Blood Type**

This bar chart displays the count of different blood types for both male and female patients. It helps in understanding the distribution of blood types across genders.

![Power BI Desktop 9_8_2024 11_16_26 PMmm](https://github.com/user-attachments/assets/28fb0051-d51e-4034-a229-c29418f6fc84)

**Test Results Breakdown**

A stacked bar chart showing the distribution of different medical conditions (e.g., Diabetes, Cancer, Hypertension) categorized by admission type (Elective, Emergency, Urgent).

![Power BI Desktop 9_8_2024 11_16_07 PMm](https://github.com/user-attachments/assets/cca86079-b16e-4e5e-9ffc-b0eb4b5a0e6e)


**Gender Breakdown**

A pie chart presenting the distribution of test results across the dataset, showing the proportion of patients with Normal, Abnormal, and Inconclusive test results and a pie chart that illustrates the gender split in the dataset, offering a quick snapshot of the male-to-female ratio.

![Power BI Desktop 9_88_2024 11_16_07 PM](https://github.com/user-attachments/assets/f8238234-1fa2-4507-9f06-ca35ce04670d)

**Binary Classification:**

Predicting Test Results (Normal vs. Abnormal)

![Jupyter Notebook - Notebook - Google Chrome 9_8_2024 11_48_14 PM](https://github.com/user-attachments/assets/7e195303-53bd-4a7d-a86d-31ab132e8962)

**Data Preparation:**

Label Encoding: It encodes the target variable Test Results for binary classification.

One-Hot Encoding: Categorical columns like 'Gender', 'Blood Type', 'Medical Condition', etc., are transformed into numerical columns using one-hot encoding.

Handling Missing Values: The code removes any rows with missing values using dropna().

Feature Scaling: Numeric columns 'Age' and 'Billing Amount' are scaled using StandardScaler(), which is a common preprocessing step for machine learning.

Splitting the Data: The dataset is split into training and testing sets using an 80/20 split ratio.

The result is a training set with 21,541 rows and 25 features and a test set with 5,386 rows and 25 features.




