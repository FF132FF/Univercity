import csv
import re

def csv_extract():

    with open('books.csv', 'r', ) as file:
        fixed_text = ""
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            fixed_text = fixed_text+str(row)+"\n"
        #fixed_text = fixed_text.replace("[", "").replace("]", "").replace("'", "")
        #fixed_text = fixed_text.replace("isbn|title|author|quantity|price", "").replace("\n", "", 1)
        #fixed_text = fixed_text[::-1].replace("\n", "", 1)
        #fixed_text = fixed_text[::-1]
    return fixed_text
def search(content):
    pattern3 = r"((\d+)-(\d+)-(\d+)-(\d+)-(\d+))[|]([^|]+)[|]([^|]+)[|](\d+)[|](\d+.*)"
    #pattern2 = r"(\d+)[|]([^|]+)[|]([^|]+)[|](\d+)[|](\d+)"
    print(content)
    pattern = r".*"
    for element in content:
        finder = re.findall(pattern, element)
        print(finder)