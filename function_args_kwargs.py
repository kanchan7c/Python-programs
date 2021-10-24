# def add_numbers(*args):  #args come back as a tuple
#     total = 0
#     for num in args:
#         total = total + num
#     return total

# print(add_numbers(1, 4, 64, 34, 2))

# def test(name, age=27, *args, **kwargs):  #keyword args looks like a dictionary
#     pass

# def person(**kwargs):
#     print(kwargs)
#     if 'brain' in kwargs:
#         print(kwargs.get("name"), " is a ", kwargs.get("brain"), " dog")

# person(name="Cookie", age= 1, brain="Dumb", fav_food="Chicken")

def order_pizza(name, address, **toppings):
    if address == None:
        address = input("Address not found, enter your address to proceed:  ")
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 150.00
    for key, value in toppings.items():
        price = price + 20
    print(f"Total price is {price}")
    return price
        
total_price = order_pizza("Samaira", None,  babycorn=True, onion=True, Capsicum=True, Tomato=True)
print(total_price)