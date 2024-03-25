# Importing Modules
import sys
import csv

# Check if enough arguments are provided
if len(sys.argv) < 3:
    print("Usage: python3 reader.py source_file destination_file change1 change2 change3 change4")
    sys.exit(1)

# Get the source_file, destination_file, and changes from CMD
source_file = sys.argv[1]
destination_file = sys.argv[2]
changes = sys.argv[3:]

# Check if changes are provided
if not changes:
    print("No changes provided!")
    sys.exit(1)


try:
    # Open the source CSV file for reading
    with open(source_file, "r") as file:
        # Read the CSV file and convert it into a list of lists
        reader = list(csv.reader(file))
        print("\nOriginal CSV content:\n")
        for content_before in reader:
            print(",".join(content_before))
except FileNotFoundError:
    print(f"\nFile not found: {file}")
    sys.exit(1)

try:
    for change in changes:
        # Split each change into its components: column, row, and value
        column, row, value = map(str.strip, change.split(","))

        # Convert column and row to integers
        column = int(column) - 1
        row = int(row) - 1

        # Update the value in the specified cell of the CSV data
        reader[row][column] = value

except ValueError or IndexError:
    print("\nplease retry!")
    sys.exit(1)

try:
    with open(destination_file, "w", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerows(reader)
except IOError:
    print(f"\nError writing in file: {destination_file}")

print("\nModified CSV Content:\n")
for content_modified in reader:
    print(",".join(content_modified))
print("")