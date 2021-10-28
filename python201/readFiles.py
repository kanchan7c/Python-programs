with open('readme.txt', 'r') as file: #file is a variable name
   print(file.read()) #doesn't give access to file outside indentation
   content = file.read() #as the file content is stored in a variable now, it gives access to the content outside the scope of the indentation

print(file.read()) #this is out of scope hence won't work
print(content) #this has the file content and will work



