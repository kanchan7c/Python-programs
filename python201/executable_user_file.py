filename = input("What is the file name? ")
content = input("Enter the content: ")

with open(filename, 'w') as file:
    file.write(content)

open_file = input("Would you like to read this file? y/n ")
if open_file in ['y','n']:
    if open_file == 'y':
        with open(filename, 'r') as file:
            print(file.read())