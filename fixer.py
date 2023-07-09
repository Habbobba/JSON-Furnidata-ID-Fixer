import json
import os
import logging
import datetime

# Configure logging
log_folder = "logging"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
logging.basicConfig(filename=log_file, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fix_ids(data, start_id, set_offerid):
    try:
        for item in data:
            item['id'] = start_id
            if set_offerid:
                item['offerid'] = start_id
            else:
                item['offerid'] = -1
            start_id += 1
    except KeyError as e:
        logging.error(f"KeyError: {e}")
        raise

# Define the file paths
input_file_path = 'furnidata/furnidata.json'
output_file_path = 'repaired/furnidata.json'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

try:
    # Read JSON data from input file
    with open(input_file_path, 'r') as file:
        json_data = json.load(file)

    # Prompt the user to enter the starting ID
    start_id = int(input("Enter the starting ID: "))

    # Prompt the user to choose whether to set offerid as id
    set_offerid_input = input("Do you want the 'offerid' to be the same as 'id'? (yes/no): ")
    set_offerid = set_offerid_input.lower() == 'yes'

    # Call the function to fix the IDs and set offerid as desired
    fix_ids(json_data['roomitemtypes']['furnitype'], start_id, set_offerid)

    # Write the repaired entries to the output file
    with open(output_file_path, 'w') as file:
        json.dump(json_data['roomitemtypes']['furnitype'], file, indent=4)

    # Print success message
    print(f"IDs fixed, offerid set as desired, and new 'furnidata.json' file with repaired entries generated in 'repaired' folder.")
except Exception as e:
    logging.exception(f"An error occurred: {e}")
    print("An error occurred. Please check the error log for more details.")