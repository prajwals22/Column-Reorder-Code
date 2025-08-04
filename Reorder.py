import pandas as pd
from openpyxl import load_workbook

# Load the workbook (optional here, unless you want to use openpyxl features)
workbook = load_workbook('File_Name.xlsx')
worksheet = workbook.active

# Read Excel file into a DataFrame
df = pd.read_excel('File_Name.xlsx')

# Define desired column order
new_order = ['Name', 'Age', 'City', 'Email']

# Reorder columns
df_reordered = df[new_order]

# Save the reordered DataFrame to a new Excel file
df_reordered.to_excel('reordered_File_Name.xlsx', index=False)

print("✅ Excel file has been reordered and saved as 'reordered_File_Name.xlsx'")
