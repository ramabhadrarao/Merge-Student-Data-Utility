import csv

# Read studentdata.csv and store data in a dictionary with 'name' as key
data_dict = {}
with open('studentdata.csv', newline='') as data_file:
    data_reader = csv.DictReader(data_file)
    for row in data_reader:
        if 'name' in row:
            data_dict[row['name']] = {
                'gender': row.get('gender', ''),
                'studentmobile': row.get('studentmobile', ''),
                'fathermobil': row.get('fathermobil', ''),
                'AdmnDate': row.get('AdmnDate', '')
            }

# Create a new CSV file 'finallist.csv' for the final results
with open('studentlist.csv', newline='') as list_file, open('finallist.csv', 'w', newline='') as final_file:
    list_reader = csv.DictReader(list_file)
    final_writer = csv.writer(final_file)

    # Write headers for the final file
    final_writer.writerow(['id', 'regdno', 'name', 'gender', 'studentmobile', 'fathermobil', 'AdmnDate'])

    # Iterate through each row in studentlist.csv
    for row in list_reader:
        name = row.get('name')  # Get the 'name' field

        # If 'name' is not present, continue to the next row
        if not name:
            continue

        if name in data_dict:
            # If the name is found in studentdata.csv, write the corresponding data to finallist.csv
            final_writer.writerow([
                row.get('id', ''),  # Get 'id' field, if it doesn't exist, write an empty string
                row.get('regdno', ''),  # Get 'regdno' field, if it doesn't exist, write an empty string
                name,
                data_dict[name]['gender'],
                data_dict[name]['studentmobile'],
                data_dict[name]['fathermobil'],
                data_dict[name]['AdmnDate']
            ])
        else:
            # If the name is not found, write only id, regdno, and name to finallist.csv
            final_writer.writerow([row.get('id', ''), row.get('regdno', ''), name])
