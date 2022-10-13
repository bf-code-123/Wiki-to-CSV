import csv
from tokenize import Name

file = open("phonebook.csv", "a")

name = input("Name: ")
print(name)
number = input("Number: ")
print(number)

writer = csv.writer(file)
writer.writerow([name, number])

file.close()