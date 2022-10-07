#------------------------
#sheaberger_finalproject
#shea berger
#may 3 2022
#------------------------


#---lists---#

grocery_list = [] #what is in cart
prices = [] # prices of the groceries

#---functions---#

# gets the user to make their list
def make_list():
    print("When your list is complete input 'done'.")
    while True:
        item = input("What are you shopping for today?")
    
        if item == "done":
            break
    
        else:
            grocery_list.append(item)

# tells the user what the cost of their items are
done = 0
def price_list():
    while True:
        price = input("What are the prices of your items?")
        
        if price == "done":
            break
        
        else:
            prices.append(int(price))

def double_check():
    check = input("Would you like to add or remove anything from the cart?")
    if check == "y":
        double = 1
    else:
        double = 2
        print("Thanks.")
        print(sum(prices))
    if double == 1:
         if "y" in check.lower():
            specify = input("please specify if you are adding or subtracting")
            if "a" in specify.lower():
                add_object = input("What would you like to add?")
                grocery_list.append(add_object)
                print(grocery_list)
                add_price = int(input("How much does the new item cost?"))
                prices.append(add_price)
                print(prices)
                print(sum(prices))
                double = 2
            
            else:
                print(grocery_list)
                number = input("Whats the name of the item you want removed? ")
                grocery_list.remove(number)
                cost = int(input("How much did that item cost? "))
                prices.remove(cost)
                print(grocery_list)
                print(prices)
                double_check()
                
         else:
             print("Okay goodbye")
             double = 2
#---Main code---#
make_list()
price_list()
print(grocery_list)
print(prices)
print("The some of the prices is:")
print(sum(prices))
double_check()

