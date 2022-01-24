import csv

with open('sample.csv', 'r') as my_csv_file:
    my_csv_reader = csv.DictReader(my_csv_file) #decided to use a dictionary
    count_lines = 0
    for row in my_csv_reader:
        if count_lines == 0:
            print(f'Our headers are {", ".join(row)}')
            count_lines += 1
        print(f'\t{row["User"]} worked {row["Duration"]} hours on {row["Description"]}') 
        count_lines += 1
    print(f'Run through {count_lines} lines.') #thought it would be good to know the number of lines in our file
    
    #not sure about the report, i need to figure it out :( 
