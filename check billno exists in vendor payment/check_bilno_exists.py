import pandas as pd
import psycopg2

# Database connection details
db_config = {
    'dbname': 'bis-erp-migration',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5433'
}

# Function to get all values from the database column


def get_values_from_db(query):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    # Extract the first column from each row
    return [str(row[0]) for row in results]  # Convert to string

# Function to check if a value exists in an Excel column


def check_values_in_excel(file_path, column_name, values):
    df = pd.read_excel(file_path)  # Load the Excel file
    # Convert the Excel column values to strings
    excel_values = df[column_name].astype(str).values

    # List to store the results
    results = []

    # Check each DB value in the Excel column
    for value in values:
        if value in excel_values:
            results.append((value, 'Found'))
        else:
            results.append((value, 'Not Found'))

    return results

# Function to save results to an Excel file


def save_results_to_excel(results, output_file):
    df = pd.DataFrame(results, columns=['BillNo', 'Found'])  # Create DataFrame
    # Save to Excel without the index column
    df.to_excel(output_file, index=False)


if __name__ == "__main__":
    # SQL query to get the values from the database
    # Adjust this query as needed
    sql_query = 'SELECT "PO_Desc" FROM "001"."PurchaseOrder"'

    # Get all values from the database
    db_values = get_values_from_db(sql_query)

    if db_values:
        # Path to the Excel file and column to check
        excel_file_path = 'D:\\IGS\\PB Data Utils Scripts\\check billno exists in vendor payment\\input\\Vendor Payment.xlsx'
        excel_column_name = 'BillNo'

        # Check the values from the database against the Excel column
        results = check_values_in_excel(
            excel_file_path, excel_column_name, db_values)

        # Output file path
        output_excel_path = 'D:\\IGS\\PB Data Utils Scripts\\check billno exists in vendor payment\\output\\output_results.xlsx'

        # Save results to Excel
        save_results_to_excel(results, output_excel_path)

        print(f"Results saved to {output_excel_path}")
    else:
        print("No values found in the database.")
