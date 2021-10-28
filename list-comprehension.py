numbers = [num**2 for num in [1, 4, 5, 2, 6]] #num is getting each number of the list one by one and getting exponent by 2. The result list is getting stored in the numbers list
print(numbers) # gives O/P [1, 16, 25, 4, 36]

baby = [ f"{item} is a baby item" for item in ["Formula", "Diaper", "Onesies", "Cookie"] if item != "Cookie" ] #another example of list comprehension
print(baby)
