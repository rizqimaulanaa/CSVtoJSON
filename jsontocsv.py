import json
import csv

# JSON Data
data = {
    "PLATFORM_ID": "TEST",
    "PASSWORD": "TEST",
    "DEVICE_NAME": "TEST",
    "METHOD": "AUTH_GetLogin",
    "DATA": {
        "PASSWORD": "PASS"
        
    }
}

csv_filename = 'output.csv'

# Functions
def write_to_json(data, json_filename):
    with open(json_filename, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4, separators=(',', ': ')))

def read_existing_csv(csv_file):
    existing_data = []
    try:
        with open(csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                existing_data.append(row)
    except FileNotFoundError:
        pass
    return existing_data

def write_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

# Extract data from the JSON structure
platform_id = data.get("PLATFORM_ID", "")
password = data.get("PASSWORD", "")
device_name = data.get("DEVICE_NAME", "")
method = data.get("METHOD", "")
data_password = data.get("DATA", {}).get("PASSWORD", "")

existing_data = read_existing_csv(csv_filename)

# Write data to CSV
with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header
    csvwriter.writerow(["PLATFORM_ID", "PASSWORD", "DEVICE_NAME", "METHOD", "DATA.PASSWORD", "DATA.USERNAME"])
    
    # Write data row

# Read existing data from the CSV
existing_data = read_existing_csv(csv_filename)

# Add new data to existing data
for i in range(1, 101):  # Loop from 1 to 100
    data_username = f"TEST_ID{i}"
    new_row = [platform_id, password, device_name, method, data_password, data_username]
    existing_data.append(new_row)

# Write updated data to CSV
write_to_csv(existing_data, csv_filename)

print(f'CSV file "{csv_filename}" updated successfully.')
