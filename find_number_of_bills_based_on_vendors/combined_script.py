import pandas as pd
from sqlalchemy import create_engine, text  # Import the text function

# Database connection setup for PostgreSQL
# Replace 'user', 'password', 'host', 'port', and 'dbname' with your actual PostgreSQL credentials
engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5433/bis-erp-migration')

# Load the first Excel file
# Replace with your file path
file1 = r'D:\IGS\PB Data Utils Scripts\find_number_of_bills_based_on_vendors\input_files\filtered_bill_header_without_filtering_material_type.xlsx'
df1 = pd.read_excel(file1)

# Load the second Excel file
# Replace with your file path
file2 = r'D:\IGS\PB Data Utils Scripts\find_number_of_bills_based_on_vendors\input_files\combined_in_progress_projects_stock_records.xlsx'
df2 = pd.read_excel(file2)

# Count occurrences of each VendorName (No of bills)
vendor_counts = df1['VendorName'].value_counts().reset_index()
vendor_counts.columns = ['VendorName', 'No of bills']

# Initialize lists to store additional information
total_items = []
vendor_status = []
material_types = []

# Open a connection to the database for checking vendor existence
with engine.connect() as connection:
    # Loop through each unique VendorName
    for vendor in vendor_counts['VendorName']:
        # Get BillNos and MaterialType for the current vendor
        vendor_data = df1[df1['VendorName'] == vendor]
        bill_nos = vendor_data['BillNo']
        # Assuming one MaterialType per vendor
        material_type = vendor_data['MaterialType'].iloc[0]

        # Append the MaterialType to the list
        material_types.append(material_type)

        # Count total rows in the second file for these BillNos (No of items)
        count = df2[df2['BillNO'].isin(bill_nos)].shape[0]
        total_items.append(count)

        # Query the database to check if the vendor exists
        query = text(
            f'SELECT COUNT(*) FROM public."Vendor" WHERE "Vend_Name" = :value')
        result = connection.execute(query, {'value': vendor}).fetchone()[0]

        # Check if the vendor was found in the database
        found = 'Found' if result > 0 else 'Not Found'
        vendor_status.append(found)

# Add the total items count, MaterialType, and vendor existence status to the vendor_counts DataFrame
vendor_counts['No of items'] = total_items
vendor_counts['MaterialType'] = material_types
vendor_counts['Status'] = vendor_status

# Save the result to a new Excel file
output_file = r'D:\IGS\PB Data Utils Scripts\find_number_of_bills_based_on_vendors\output_files\final_output_file.xlsx'
vendor_counts.to_excel(output_file, index=False)

print("The new file has been created successfully.")
