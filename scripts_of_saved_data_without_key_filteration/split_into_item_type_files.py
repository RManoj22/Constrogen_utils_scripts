# This Python script is performing the following tasks:
import pandas as pd
import os

# Load the Excel file
# Update this if the file is in a different location
file_path = r'D:\IGS\Constrogen_data_migration\new_matched_results.xlsx'
df = pd.read_excel(file_path)

# Specify the folder where you want to save the files
output_folder = 'ItemType_Files'  # You can change the folder name as needed

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the unique values in the 'ItemTypeName' column
unique_item_types = df['ItemTypeName'].unique()

# Iterate over each unique item type to create a separate file
for item_type in unique_item_types:
    # Filter the DataFrame for rows where 'ItemTypeName' matches the current item type
    filtered_df = df[df['ItemTypeName'] == item_type]

    # Construct a safe filename by replacing or removing problematic characters
    safe_filename = f"{item_type}.xlsx".replace(
        "/", "_")  # Adjust further if needed

    # Define the complete path for the new file
    output_path = os.path.join(output_folder, safe_filename)

    # Save the filtered DataFrame to the new Excel file inside the folder
    filtered_df.to_excel(output_path, index=False)

    print(f"Created file: {output_path} with {len(filtered_df)} rows")
