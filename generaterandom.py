import csv
import random
randfile = open("Random2.csv", "w")
writer = csv.writer(randfile, delimiter = ',')

# Specify the number of rows
for i in range(10):
    # Specify number of columns
    RandomListOfIntegers = [random.randint(1, 100) for iter in range(10)]

    writer.writerow(RandomListOfIntegers)

randfile.close()

with open('Random2.csv') as in_file:
    with open('Random3.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow(row)

