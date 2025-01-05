again = True
item = ""
price = 0
while again == True:
    item = item + ", "+input("what item do you want to add")
    price=price+int(input("how much does it cost"))
    if input("y or n, do you want to add another item") != 'y':
        print("here")
        again = False
print("it costs ", end = "")
print(price, end = "")
print(" for " + item)
