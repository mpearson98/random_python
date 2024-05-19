import os
import olefile

# Define the directory to scan
directory = '/path/to/directory'

# Initialize an empty list to hold the report data
report = []

# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is an Office 365 document
        if file.endswith(('.docm', '.xlsm', '.pptm')):
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Check if the file contains macros
            if olefile.isOleFile(file_path) and 'VBA' in olefile.OleFile(file_path).listdir():
                # Add the file to the report
                report.append(file_path)

# Print the report
for file in report:
    print(file)