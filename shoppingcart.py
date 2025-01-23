again = True
item = ""    #list of items
price = 0
while again == True:
    item = item + ", "+input("what item do you want to add")    #adding items to list
    price=price+int(input("how much does it cost"))        #adding to price
    if input("y or n, do you want to add another item") != 'y':
        print("here")
        again = False
print("it costs ", end = "")
print(price, end = "")
print(" for " + item)
