"""
SAMPLE EXERCISE::::::
REad command line arguments
check the number of arguments
User argumetnto perform tasks (in this case, simple operations like addition and multiplication)
Access the python version and the list of paths where python modules are searched


git commit -m "some commit info"
      
          0             1  2 3
python3 sys_example.py add 2 2
python3 sys_example.py multiply 3 5
python3 ses_example.py 
"""



import sys

# print("\nInfo about python")
# print(f"Python version: {sys.version}")

# Read the operation and numbers from CMD using the 1st argument considering that pc starts from [0]

if len(sys.argv) < 4 or sys.argv[1] == "--help":
    print("Usage: python3 sys_example.py operation num1 num2")
    print("Operation can be 'add' or 'multiply'")
    sys.exit(1)

operation = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])


# num1 = sys.argv[2]
# num2 = sys.argv[3]
# If the above is run instead of int():
# $ python3 sys_example.py add 2,2 44
# The result of adding 2,2 and 44 is 2,244

# print(operation, num1, num2)

if operation == "add":
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result of multiplication {num1} and {num2} is {result}")
else:
    print("Invalid operation!")

