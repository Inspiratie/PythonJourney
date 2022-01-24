import csv

with open('sample.csv', 'r') as my_csv_file:
    my_csv_reader = csv.DictReader(my_csv_file)
    count_lines = 0
    for row in my_csv_reader:
        if count_lines == 0:
            print(f'Column names are {", ".join(row)}')
            count_lines += 1
        print(f'\t{row["User"]} worked {row["Duration"]} hours on {row["Description"]}')
        count_lines += 1
    print(f'Run through {count_lines} lines.')
