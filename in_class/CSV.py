import csv

with open('users.csv', 'r', encoding='utf-8' ) as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

    # ['Mike', 'Dow', '33', '456-34-12']

with open('users.csv', 'a', newline='' ) as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['John', 'Smith', 25, '123-45-67'])