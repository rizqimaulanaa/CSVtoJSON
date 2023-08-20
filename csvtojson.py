import csv
import json

csv_file = 'output.csv'

def write_to_json(data, json_filename):
    with open(json_filename, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

def csv_to_multiple_json(csv_file):
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        for i, row in enumerate(csvreader, start=1):
            platform_id = row.get("PLATFORM_ID", "")
            password = row.get("PASSWORD", "")
            device_name = row.get("DEVICE_NAME", "")
            method = row.get("METHOD", "")
            data_password = row.get("DATA.PASSWORD", "")
            data_username = row.get("DATA.USERNAME", "")

            json_data = {
                "PLATFORM_ID": platform_id,
                "PASSWORD": password,
                "DEVICE_NAME": device_name,
                "METHOD": method,
                "DATA": {
                    "PASSWORD": data_password,
                    "USERNAME": data_username
                }
            }

            json_filename = f'{i}.json'
            write_to_json(json_data, json_filename)
            print(f"Row {i} data saved to {json_filename}")

    print("CSV to multiple JSON files conversion successful.")

csv_to_multiple_json(csv_file)
