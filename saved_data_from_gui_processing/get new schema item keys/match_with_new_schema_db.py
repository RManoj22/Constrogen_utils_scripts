import pandas as pd
import psycopg2

# PostgreSQL connection setup
conn = psycopg2.connect(
    host="localhost",
    dbname="bis-erp-migration",
    user="postgres",
    password="postgres",
    port="5433"
)

# Read input Excel file
input_file = 'D:\IGS\PB Data Utils Scripts\saved_data_from_gui_processing\input files\matched_items_from_saved_data.xlsx'
df = pd.read_excel(input_file)

# Convert 'Current Item Description' to title case and strip spaces
df['Current Item Description'] = df['Current Item Description'].str.strip().str.title()

# Function to get Item_Key and Item_Descr from the database
def get_item_info(item_descr):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT "Item_Key", "Item_Descr" FROM "001"."Item"
                WHERE "Item_Descr" = %s
                LIMIT 1;
            """, (item_descr,))
            result = cur.fetchone()
            if result:
                return result[0], result[1]  # Return both Item_Key and Item_Descr
            else:
                return None, None  # Return None if no match is found
    except Exception as e:
        print(f"Error retrieving data for {item_descr}: {e}")
        return None, None

# Apply the function to get Item_Key and Item_Descr and store in new columns
df[['Schema key', 'Matched description']] = df['Current Item Description'].apply(
    lambda descr: pd.Series(get_item_info(descr))
)

# Write the result to a new Excel file
output_file = 'output_file.xlsx'
df.to_excel(output_file, index=False)

# Close the database connection
conn.close()

print(f"Data written to {output_file}")
