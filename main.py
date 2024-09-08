import pandas as pd

# Load the dataset
file_path = 'healthcare_dataset.csv'
df = pd.read_csv(file_path)

# Standardize capitalization for text columns, including 'Name' to avoid case-sensitive duplicates
text_columns = ['Name', 'Gender', 'Medical Condition', 'Doctor', 'Hospital', 'Admission Type', 'Medication']

def clean_text(column):
    return column.str.strip().str.title()  # Strip spaces and title-case each word

for col in text_columns:
    if col in df.columns:
        df[col] = clean_text(df[col])

# Check for duplicate rows based on the 'Name' column after standardizing capitalization
duplicates = df[df.duplicated(subset='Name', keep=False)]

if not duplicates.empty:
    print(f"Number of duplicate names: {duplicates.shape[0]}")
    print("Duplicate Entries:")
    print(duplicates)
else:
    print("No duplicate names found.")

# Remove duplicate rows based on 'Name', keeping the first occurrence
df.drop_duplicates(subset='Name', keep='first', inplace=True)

# After removing duplicates, check the number of rows left
print(f"\nNumber of rows after removing duplicate names: {df.shape[0]}")

# Check if 'Date of Admission' and 'Discharge Date' are in proper date format
def check_date_format(date_column):
    try:
        pd.to_datetime(df[date_column], errors='raise')
        print(f"All dates in {date_column} are valid.")
    except ValueError as e:
        print(f"Issue with dates in {date_column}: {e}")

check_date_format('Date of Admission')
check_date_format('Discharge Date')

# Save the cleaned dataset without duplicates
cleaned_file_path = 'cleaned_healthcare_dataset_no_duplicates.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned dataset saved to '{cleaned_file_path}'.")
