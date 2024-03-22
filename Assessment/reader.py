import sys
import csv



if len(sys.argv) < 6:
    print("Usage: python3 reader.py source_file destination_file change1 change2 change3 change4")
    sys.exit(1)


source_file = sys.argv[1]
# destination_file = sys.argv[2]
# change1 = sys.argv[3]
# change2 = sys.argv[4]
# change3 = sys.argv[5]
# change4 = sys.argv[6]


if source_file == "in.csv":
    with open("in.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

# elif destination_file == "out.csv":
#     # WRITE to file here
#     print("lalalsssss")

# else:
#     print("Invalid command!")