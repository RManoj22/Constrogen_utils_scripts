"""
This script takes a excel file which has the item key to be retained and a list of purpose keys for each items as input
and populates the item purpose table which is a many to many relation between item and purpose
so this script takes single item key and populates the table with number of purpose keys it has 
"""

import psycopg2
import pandas as pd

db_params = {
    'dbname': 'bis-erp-migration',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5433
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**db_params)

    # Read the Excel file
    df = pd.read_excel(
        r'D:\IGS\PB Data Utils Scripts\item_purpose_table_populating\input_files\Item_keys_retained.xlsx'
    )

    # Use a cursor to interact with the database
    with conn:
        with conn.cursor() as cursor:
            # Iterate over the DataFrame
            for index, row in df.iterrows():
                retained_key = row['Retained_Key']
                purpose_keys = row['Purpose_Keys']
                # Clean and parse the purpose keys (remove curly brackets and split by comma)
                purpose_keys = purpose_keys.strip('[]').split(',')

                # Insert each purpose key into the ItemPurpose table in the specified schema
                for purpose_key in purpose_keys:
                    purpose_key = purpose_key.strip()  # Clean up any whitespace
                    # Create a query for inserting the values with schema specified
                    query = """
                    INSERT INTO "001"."ItemPurpose" ("ItemPurpose_ItemKey", "ItemPurpose_PurposeKey", "ItemPurpose_ClientID")
                    VALUES (%s, %s, %s);
                    """
                    # Execute the query with parameters
                    try:
                        cursor.execute(query, (retained_key, purpose_key, 1))
                    except Exception as e:
                        print(
                            f"Error inserting ({retained_key}, {purpose_key}): {e}")
                        # Rollback the transaction if there is an error
                        conn.rollback()
                        # Optionally, break the loop if you want to stop processing on error
                        break
            else:
                # If no errors occurred, commit the transaction
                conn.commit()
except Exception as ex:
    print(f"Database connection error: {ex}")
finally:
    # Close the connection
    if conn:
        conn.close()

print("Script execution completed.")
