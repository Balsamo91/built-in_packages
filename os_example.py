import os

# Get the list of all the files within the directory

files = os.listdir('.') # The '.' shows all the files that are in the current directory

print("File: ")
for file in files:
    print(file)



# Creat a folder
os.mkdir('New_folder')

print(os.name)




# Remove a Folder
# os.rmdir('New_folder')




