import sys  # Import the sys module to access command-line arguments
import csv  # Import the csv module to handle CSV files

# Check if enough command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python3 reader.py source_file destination_file change1 change2 change3 change4")
    sys.exit(1)  # Exit the program with a status code of 1 if there are not enough arguments

# Get the source file, destination file, and changes from command-line arguments
source_file = sys.argv[1]
destination_file = sys.argv[2]
changes = sys.argv[3:]

# Check if changes are provided
if not changes:
    print("No changes provided!")  # Print a message if no changes are provided
    sys.exit(1)  # Exit the program with a status code of 1

try:
    # Open the source CSV file for reading
    with open(source_file, "r") as file:
        reader = list(csv.reader(file))  # Read the CSV file and convert it into a list of lists
        print("\nOriginal CSV content:\n")  # Print a message to indicate the original CSV content
        for content_before in reader:  # Iterate over each row in the original CSV content
            print(",".join(content_before))  # Print each row of the original CSV content
except FileNotFoundError:
    print(f"\nFile not found: {source_file}")  # Print an error message if the source file is not found
    sys.exit(1)  # Exit the program with a status code of 1

try:
    for change in changes:
        # Split each change into its components: column, row, and value
        column, row, value = map(str.strip, change.split(","))
        
        # Convert column and row to integers and adjust to start indexing from 0
        column = int(column) - 1  # Convert the column number to an integer and subtract 1 to adjust indexing
        row = int(row) - 1  # Convert the row number to an integer and subtract 1 to adjust indexing
        
        # Update the value in the specified cell of the CSV data
        reader[row][column] = value  # Assign the new value to the specified cell in the CSV data

except (ValueError, IndexError):
    print("\nPlease retry!")  # Print an error message if there's an issue with the changes
    sys.exit(1)  # Exit the program with a status code of 1

try:
    # Open the destination CSV file for writing
    with open(destination_file, "w", newline="") as file2:
        writer = csv.writer(file2)  # Create a CSV writer object
        writer.writerows(reader)  # Write the modified CSV data to the destination file
except IOError:
    print(f"\nError writing in file: {destination_file}")  # Print an error message if there's an issue writing to the destination file

print("\nModified CSV Content:\n")  # Print a message to indicate the modified CSV content
for content_modified in reader:  # Iterate over each row in the modified CSV content
    print(",".join(content_modified))  # Print each row of the modified CSV content
print("")  # Print an empty line for better formatting
