from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

Menu= {"Idly" : 25, 
       "Dosa" : 50, 
       "Vada" : 20, 
       "Pongal" : 40, 
       "Poori" : 40,
       "Idiyappam" : 35,
       "Coffee" : 15, 
       "Tea" : 10}

Order ={}
Order_type = ""
Packing_Charge = 10

def Select_Order_Type():
    global Order_type
    print("Select Order Type:")
    print("1. Dine-In")
    print("2. Take-away")

    Choice = int(input("Enter the Order type (1 or 2):"))

    if Choice == 1:
        Order_type = "Dine-In"
    elif Choice == 2:
        Order_type = "Take-away"        
    else:
        print("Invalid Choice! Please select again.")
    
def Display_Menu():
    print("---Menu---:")
    for item, price in Menu.items():
        print(f"{item}- Rs.{price}")
    print("---***---")

def Place_Order():
    item = input("Enter the item you want to order:").title()
    if item in Menu:
        quantity = int(input(f"Enter the No. of {item} you want to order:"))
        Order[item] = Order.get(item,0) + quantity
        print("Order Placed Successfully!")

    else:
        print("Item not available")

def Generate_Bill():
    print(f"------Bill---{current_date}-----")
    print(f"Order Type: {Order_type}")
    total = 0

    for item, quantity in Order.items():
        Amount = Menu[item] * quantity  
        print(f"{item} x {quantity} = Rs.{Amount}")     
        total += Amount

    if Order_type == "Take-away":
        total_items = sum(Order.values())
        packing_total = Packing_Charge * total_items
        print(f"Packing Charge ({total_items} items) = Rs.{packing_total}")
        total += packing_total

    
    print(f"Total Amount: Rs.{total}")
    print("---------------")

Select_Order_Type()

while True:
    print("1. Display Menu")
    print("2.Place Order")
    print("3.Generate Bill")
    print("4.Exit")

    Choice = int(input("ENter Your Choice:"))

    if Choice == 1:
        Display_Menu()  
    elif Choice == 2:
        Place_Order()
    elif Choice == 3:
        Generate_Bill()
    elif Choice == 4:
        print("Thank you, Visit Again!")
        break
    else:
        print("Invalid Choice! Please select again.")



