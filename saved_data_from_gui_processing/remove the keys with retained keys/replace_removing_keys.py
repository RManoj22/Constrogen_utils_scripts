"""
This script takes two excel files as input:
item retained keys file which has retained key and keys to be removed column
only match found data filtered from the saved_data file got as output from the gui

this script reads the value from a colum which is set as the new item key matched manually from the gui and 
checks whether it is one of the values in the column keys to be removed and if matches replaces it with the retained key column value

after performing this replaces it in the second file itself without creating another file for output  
"""


import pandas as pd
import ast

# Function to load Excel files


def load_excel(file_path_1, file_path_2):
    df1 = pd.read_excel(file_path_1)
    df2 = pd.read_excel(file_path_2)
    return df1, df2

# Function to replace keys based on the mapping and track replacements


def replace_keys(df1, df2):
    # Create new columns 'Replaced' and 'Old New Item Key'
    df2['Replaced'] = 'No'
    df2['Old New Item Key'] = df2['New Item Key']  # Copy original values

    # Iterate through each row of the first dataframe (df1)
    for _, row in df1.iterrows():
        retained_key = row['Retained_Key']
        keys_to_remove = row['Keys_To_Be_Removed']

        # Convert string representation of a set into an actual set
        keys_to_remove = ast.literal_eval(keys_to_remove)

        # Replace occurrences of keys in 'New Item Key' and mark replacements
        for key in keys_to_remove:
            # Find rows where the 'New Item Key' matches the key to be removed
            matching_rows = df2['Schema key'] == key

            # Replace the key in 'New Item Key' column
            df2.loc[matching_rows, 'Schema Key'] = retained_key

            # Mark the row as replaced and store the original value in 'Old New Item Key'
            df2.loc[matching_rows, 'Replaced'] = 'Yes'

    return df2

# Function to overwrite the original file with the modified dataframe


def overwrite_file(df2, output_file):
    df2.to_excel(output_file, index=False)

# Main function


def main(input_file_1, input_file_2):
    # Load the input files
    df1, df2 = load_excel(input_file_1, input_file_2)

    # Perform the replacement operation
    result = replace_keys(df1, df2)

    # Overwrite the second file with updated data
    overwrite_file(result, input_file_2)
    print(f"File {input_file_2} updated successfully!")


# Example usage
if __name__ == "__main__":
    input_file_1 = 'D:\IGS\PB Data Utils Scripts\saved_data_from_gui_processing\Item_keys_retained.xlsx'
    input_file_2 = 'D:\IGS\PB Data Utils Scripts\saved_data_from_gui_processing\match_found_items.xlsx'  # This file will be overwritten

    main(input_file_1, input_file_2)
