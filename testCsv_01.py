import csv
with open('tt1.csv', 'r+') as csvFile:
    readFile = csv.reader(csvFile)
    for row in readFile:
        print (row)