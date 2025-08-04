from openpyxl import load_workbook
import pandas as pd

# Load workbook
wb = load_workbook('File_Name.xlsx')
ws = wb.active

# Read data into pandas for easier manipulation
df = pd.read_excel('File_Name.xlsx')

# Reorder columns
new_order = ['Column A', 'Column B', 'Column C']
df_reordered = df[new_order]

# Write back to Excel
df_reordered.to_excel('reordered_File_Name.xlsx', index=False)

