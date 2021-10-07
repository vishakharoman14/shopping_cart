#Vishakha Roman.
import sys
# Creating The Menu
def mainMenu():
 while True:
  
    print("****** Shopping List******")
    print('''Select a number for the action that you would like to do:
     
            1:View Shopping Cart
            2:Add item To Shopping Cart
            3:Remove item from Shooping Cart
            4:Clear Shopping Cart 
            5: Exit ''')
    selection=input("Make Your Selection:")
    if selection=="1":
        displayList()
    elif selection=="2":
        additem()
    elif selection=="3":
        removeitem()
    elif selection=="4":
        clearList()
    elif selection=="5":
        sys.exit()
    else:
        print("you did not make a valid selection.")
shopping_list=["orange","apple","milk","mango"]

#Display Shopping Cart
def displayList():
    print("*** Shopping List ***")
    for i in shopping_list:
        print("*"+i)

#Add items in cart
def additem():
    item=input("Enter the item you wish to add to the shopping cart:")
    shopping_list.append(item)
    print(item+" Has been added to your shopping cart")

# Remove items from shopping Cart
def removeitem():
    item=input("Enter the item you wish to REMOVE from shopping cart:")
    shopping_list.remove(item)
    print(item+" Has been Removed from your shopping cart")

#clear Shopping Cart
def clearList():
    
    shopping_list.clear()
    print("The Shopping Cart is Empty now.")

mainMenu()