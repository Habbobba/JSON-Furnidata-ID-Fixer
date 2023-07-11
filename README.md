# Furnidata JSON Fixer

This script is used to fix the IDs in a furnidata JSON file and optionally set the 'offerid' as the same value as the 'id' for each entry.

## Usage

1. Download or clone the repository to your local machine.

2. Navigate to the project directory.

3. Place the `furnidata.json` file you want to fix in the `furnidata` directory within the project directory.

4. Open a terminal or command prompt and navigate to the project directory.

5. Run the script using the following command:

   ```
   python fixer.py
   ```

6. The script will prompt you to enter the starting ID. Please enter a numeric value to set the starting range for the IDs.

7. The script will then ask whether you want the 'offerid' to be the same as 'id' for each entry. Enter 'yes' or 'no' to choose.

   - If you choose 'yes', the 'offerid' will be set as the same value as the 'id' for each entry.
   - If you choose 'no', the 'offerid' will be set to -1 for each entry.

8. After processing the JSON file, the script will generate an updated `furnidata.json` file in the `repaired` directory within the project directory.

9. The script will display a success message indicating that the IDs have been fixed and the new `furnidata.json` file has been generated.

10. You can find the updated `furnidata.json` file in the `repaired` directory.

## Notes

- The input `furnidata.json` file should be placed in the `furnidata` directory before running the script.
- The script will create the `repaired` directory if it doesn't already exist.
- Make sure you have the necessary read and write permissions for the directories and files involved.

## Credits

This script was created by Gizmo.

## Donate

If you wish to donate, please contact Gizmo#1813 on Discord.
