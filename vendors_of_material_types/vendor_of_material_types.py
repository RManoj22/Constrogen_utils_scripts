import pandas as pd

# Read the input Excel file
input_file = r'D:\IGS\PB Data Utils Scripts\vendors_of_material_types\input\filtered_bill_header_without_filtering_material_type.xlsx'  # Replace with your actual input file path
df = pd.read_excel(input_file)

# Group the data by MaterialType and collect VendorNames
grouped_df = df.groupby('MaterialType')['VendorName'].apply(
    lambda x: ', '.join(x.unique())).reset_index()

# Save the result to a new Excel file
# Replace with your desired output file path
output_file = r'D:\IGS\PB Data Utils Scripts\vendors_of_material_types\output\output_file.xlsx'

print(f"Data has been successfully written to {output_file}")
