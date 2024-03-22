import csv

# Data example

data = [
    ["name", "age", "city"],
    ["Alice", 25, "Boston"],
    ["Bob", 30, "Chicago"]
]

# Writing in csv file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Using dict writer to write to a csv
        
fieldnames = ["name", "age", "city"]
person1 = {
    'name': 'Alice',
    'age': 25,
    'city': 'Boston'
}

person2 = {
    'name': 'Bob',
    'age': 30,
    'city': 'Chicago'
}

with open('example_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(person1)
    writer.writerow(person2)


# REading using dict reader
    
with open('example_dict.csv', 'r') as file:
    writer = csv.DictReader(file)
    print(writer)
