import os
import pandas as pd

# Set the directory containing the CSV files
directory = os.getcwd()

# Create an empty DataFrame to store the combined data
combine_or_check = input("Do you want to combine document (1) or to check attendance (2)? ")
what = input("What to combine? sign up atendees (s), workshop attendence (w), zoom attendence(z)? ")
combined_data = pd.DataFrame()
online_instructor = 'Huu Quang Nhat Nguyen'
match combine_or_check:
    case "1":
# Loop through all CSV files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):
                # Read in the CSV file
                file_path = os.path.join(directory, filename)
                data = pd.read_csv(file_path)
                # Combine the data with the existing data
                combined_data = pd.concat([combined_data, data], ignore_index=True)
        match what:
            case "s":
                # Remove duplicates based on the EmailAddress column
                combined_data = combined_data.drop_duplicates(subset=['EmailAddress'])

                # Drop specified columns
                columns_to_drop = ['Discount', 'Credit', 'PaymentType', 'PaymentInfo', 'Comment', 'Cost']
                combined_data = combined_data.drop(columns_to_drop, axis=1)

                # Remove anyone who has 'Cancelled' in the Status column
                combined_data = combined_data[combined_data['Status'] != 'Cancelled']

                # Sort the combined data by the FirstName column
                combined_data = combined_data.sort_values(by=['FirstName'])

                # Write the combined data to an Excel file called "finalize.xlsx"
                combined_data.to_excel("finalize.xlsx", index=False)
            case "w":
                pass
            case "z":
                # Remove duplicates based on the EmailAddress column
                combined_data = combined_data.drop_duplicates(subset=['Name (Original Name)'])

                # Drop specified columns
                columns_to_drop = ['Total Duration (Minutes)', 'Guest']
                combined_data = combined_data.drop(columns_to_drop, axis=1)

                # Remove the instructor from the data
                combined_data = combined_data[combined_data['Name (Original Name)'] != online_instructor]

                # Sort the combined data by the FirstName column
                combined_data = combined_data.sort_values(by=['Name (Original Name)'])

                # Write the combined data to an Excel file called "finalize.xlsx"
                combined_data.to_excel("finalize.xlsx", index=False)
                
    case "2":
        pass
        