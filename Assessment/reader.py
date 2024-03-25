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
        for content_before in reader: # Iterate over each row in the original CSV content
            print(",".join(content_before)) # Print each row of the original CSV content
# Print an error message if the source file is not found
except FileNotFoundError:
    print(f"\nFile not found: {file}")
    sys.exit(1)

try:
    for change in changes:
        # Split each change into its components: column, row, and value
        column, row, value = map(str.strip, change.split(","))

        # Convert column and row to integers
        column = int(column)
        row = int(row)

        # Update the value in the specified cell of the CSV data
        reader[row][column] = value

# Print an error message if there's an issue with the changes
except ValueError or IndexError:
    print("\nplease retry!")
    sys.exit(1)

try:
    # Open the destination CSV file for writing
    with open(destination_file, "w", newline="") as file2:
        writer = csv.writer(file2) # Create a CSV writer object
        writer.writerows(reader) # Write the modified CSV data to the destination file
# Print an error message if there's an issue writing to the destination file
except IOError:
    print(f"\nError writing in file: {destination_file}")

print("\nModified CSV Content:\n")
# Iterate over each row in the modified CSV content
for content_modified in reader:
    print(",".join(content_modified)) # Print each row of the modified CSV content
print("") # Print an empty line