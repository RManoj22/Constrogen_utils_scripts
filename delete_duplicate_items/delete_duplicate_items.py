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
        r'D:\IGS\PB Data Utils Scripts\delete_duplicate_items\input_file\Item_keys_retained.xlsx'
    )

    # Use a cursor to interact with the database
    with conn:
        with conn.cursor() as cursor:
            # Iterate over the DataFrame
            for index, row in df.iterrows():
                item_keys_to_delete = row['Keys_To_Be_Removed']
                print('item_keys_to_delete', item_keys_to_delete)
                item_delete_keys = item_keys_to_delete.strip('[]').split(',')
                print('item_delete_keys', item_delete_keys)

                for item_key in item_delete_keys:
                    item_key = item_key.strip()
                    print('item_key after strip', item_key)

                    # First delete from ItemSpecification table
                    delete_spec_query = """
                    DELETE FROM "001"."ItemSpecification" WHERE "ItemSpec_Item_key" = %s;
                    """
                    try:
                        cursor.execute(delete_spec_query, (item_key,))
                    except Exception as e:
                        print(f"Error deleting from ItemSpecification for ({item_key}): {e}")
                        conn.rollback()
                        break

                    # Then delete from Item_ItemUOM table
                    delete_uom_query = """
                    DELETE FROM "001"."Item_ItemUOM" WHERE "ItemItemUOM_Item_Key" = %s;
                    """
                    try:
                        cursor.execute(delete_uom_query, (item_key,))
                    except Exception as e:
                        print(f"Error deleting from Item_ItemUOM for ({item_key}): {e}")
                        conn.rollback()
                        break

                    # Now delete from Item table
                    delete_item_query = """
                    DELETE FROM "001"."Item" WHERE "Item_Key" = %s;
                    """
                    try:
                        cursor.execute(delete_item_query, (item_key,))
                    except Exception as e:
                        print(f"Error deleting ({item_key}): {e}")
                        conn.rollback()
                        break
                else:
                    # If no errors occurred, commit the transaction
                    conn.commit()
except Exception as ex:
    print(f"Database connection error: {ex}")
finally:
    if conn:
        conn.close()

print("Script execution completed.")
