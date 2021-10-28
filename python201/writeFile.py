with open('writing_files.txt', 'w') as file: #file writing_files.txt will be dynamically created and write command will be executed. 'w' overwrites the file when the code is executed again
    file.write("This is written by Python") #file will be written with the text in quotes

with open('writing_files.txt', 'a') as file: # 'a' will add the content instead of overwriting the file
    file.write("\nThis is a second line appended") #this will be written in the file. Use '\n' to append in a new line. '\t' to add indentation

