words = {"Glory":"high renown or honour won by notable achievements",
         "Quarter" : "each of four equal or corresponding parts into which something is or can be divided",
         "Ambience" : "the character and atmosphere of a place" ,
         "Gracious" : "courteous, kind, and pleasant, especially towards someone of lower social status"}
print("Enter the word:")
look = input()
if look in words:
 print(words[look])
else:
 print("Please select from Glory, Quarter, Ambience or Gracious")
