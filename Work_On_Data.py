import csv

input_file_path = 'First_Data_Base.csv'
output_file_path = 'Final_Data_Base.csv'

with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    first_row = next(reader)
    first_row = first_row[:3] + first_row[4:]
    writer.writerow(first_row)
    for row in reader:
        try:
            row[3] = float(row[3])
        except ValueError:
            row[3] = 0
        writer.writerow(row)



