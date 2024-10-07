# This Python script is performing the following tasks:
import pandas as pd

# Load the Excel files
book1 = pd.read_excel(r"C:\Users\666rm\Downloads\Book1.xlsx")
matched_item_result = pd.read_excel(
    r"D:\IGS\Constrogen_data_mIgration_gui\input_files\matched_items_result.xlsx")

# Extract the values from the 'S.No' column in book1
sno_values = book1['S.No'].unique()

# Filter matched_item_result based on matching 'SNo' values in book1
filtered_data = matched_item_result[matched_item_result['SNo'].isin(
    sno_values)]

# Save the filtered data to a new Excel file
filtered_data.to_excel('new_matched_results.xlsx', index=False)

print("New file with filtered data from matched_item_result has been created.")
