import zipfile
import os


zip_file_path = 'stockx.zip'
extract_dir = 'extracted_files'


if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# List all files in the extraction directory
extracted_files = os.listdir(extract_dir)


for file_name in extracted_files:
    file_path = os.path.join(extract_dir, file_name)
 
    if file_name.endswith('.csv'):
        print(f'{file_name} is already a CSV file.')
    else:

        if file_name.endswith('.json'):
            import pandas as pd
            
            json_file_path = file_path
            csv_file_path = os.path.join(extract_dir, file_name.replace('.json', '.csv'))

            df = pd.read_json(json_file_path)
            

            df.to_csv(csv_file_path, index=False)
            print(f'Converted {file_name} to CSV format.')

print('Extraction and conversion completed.')
