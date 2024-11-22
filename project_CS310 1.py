line1 = "--------------------------------------------------------"

wc_line = """
--------------------------------------------------------
                WELCOME TO Nitorpa's Food
--------------------------------------------------------
    >>>>> Please login/register for use app <<<<<
--------------------------------------------------------
    1. Login
    2. Register
    3. Exit
--------------------------------------------------------
"""

exit_line = """
--------------------------------------------------------
        Thank you for using our app service.
             Exiting the app. Goodbye!

                ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                ───█▒▒░░░░░░░░░▒▒█───
                ────█░░█░░░░░█░░█────
                ─▄▄──█░░░▀█▀░░░█──▄▄─
                █░░█─▀▄░░░░░░░▄▀─█░░█
--------------------------------------------------------
"""

payment_line = """
--------------------------------------------------------
                    Payment system
--------------------------------------------------------
    1. Credit card
    2. Cash              
--------------------------------------------------------      
"""

register_wp = """
--------------------------------------------------------
                RESISTER FOR USE Nitorpa's Food
--------------------------------------------------------
"""

login_wp = """
--------------------------------------------------------
                LOGIN TO USE Nitorpa's Food
--------------------------------------------------------
"""

menutype_line = """
--------------------------------------------------------
                WELCOME TO Nitorpa's Food
--------------------------------------------------------
                     Type Menu
--------------------------------------------------------
    ID                Menu               
    F01       Main menu       
    F02       Snack & Sweet        
    F03       Breakfast
    D01       Drink
========================================================            
    L         Logout 
    E         Exit!
======================================================== 
"""

shipping_line = """
--------------------------------------------------------
                Shipping address
--------------------------------------------------------
"""

receipt_line = """
--------------------------------------------------------
                      Receipt
--------------------------------------------------------
"""

end_line = """
--------------------------------------------------------
        Thank you for using our app service.

                ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                ───█▒▒░░░░░░░░░▒▒█───
                ────█░░█░░░░░█░░█────
                ─▄▄──█░░░▀█▀░░░█──▄▄─
                █░░█─▀▄░░░░░░░▄▀─█░░█
--------------------------------------------------------
"""

menutype_list = {
    "F01": "Main Course",
    "F02": "Snack & Sweet",
    "F03": "Breakfast",
    "D01": "Drink"
}

menu_items = {
    "F01": [
        {"ID": "M01", "Menu": "Sanders Hit", "Price": 125},
        {"ID": "M02", "Menu": "Fried Chicken Set", "Price": 145},
        {"ID": "M03", "Menu": "Kai Jai Ded Chicken Pop", "Price": 169},
        {"ID": "M04", "Menu": "Kai Suk Jai", "Price": 139},
        {"ID": "M05", "Menu": "Donjai Set", "Price": 140},
        {"ID": "M06", "Menu": "Kfc Green Curry Crispy", "Price": 89},
        {"ID": "M07", "Menu": "BBQ Wings", "Price": 99},
        {"ID": "M08", "Menu": "Spicy Tenders", "Price": 115}
    ],
    "F02": [
        {"ID": "S01", "Menu": "Sundae Ice Cream", "Price": 89},
        {"ID": "S02", "Menu": "Sweet Potato Balls", "Price": 60},
        {"ID": "S03", "Menu": "Vanilla Cake", "Price": 85},
        {"ID": "S04", "Menu": "Cookies", "Price": 55},
        {"ID": "S05", "Menu": "Chocolate Brownie", "Price": 75},
        {"ID": "S06", "Menu": "Macarons", "Price": 95},
        {"ID": "S07", "Menu": "Egg Tart", "Price": 100}
    ],
    "F03": [
        {"ID": "B01", "Menu": "Pancake & Bacon", "Price": 109},
        {"ID": "B02", "Menu": "Cheese Omelette", "Price": 95},
        {"ID": "B03", "Menu": "Fresh Fruit Salad", "Price": 119},
        {"ID": "B04", "Menu": "Granola & Yogurt", "Price": 85},
        {"ID": "B05", "Menu": "Hash Browns & Sausage", "Price": 79},
        {"ID": "B06", "Menu": "French Toast Sticks", "Price": 89}
    ],
    "D01": [
        {"ID": "D01", "Menu": "Water", "Price": 15},
        {"ID": "D02", "Menu": "Latte", "Price": 65},
        {"ID": "D03", "Menu": "Green Tea", "Price": 60},
        {"ID": "D04", "Menu": "Espresso", "Price": 65},
        {"ID": "D05", "Menu": "Matcha Latte", "Price": 75},
        {"ID": "D06", "Menu": "Hot Chocolate", "Price": 55}
    ]
}

users = {}

totalp = 0
discount = 0

def register():
    print(register_wp)
    while True: # username check
        username = input("Enter your username: ")

        if len(username) >= 5 and not username.isdigit():
            if username in users:  
                print("Username already exists.")
            else:
                break  
        else:
            print("Username must be at least 5-digit and cannot include all numbers...")

    while True: #password check
        password = input("Enter your password: ")
        if len(password) >= 8 :
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                break
            else:
                print("Password do not match. Please try again.")
        else:
            print("Please enter a 8-digit password.")
    
    while True: #email check
        email = input("Enter your email: ")
        if '@' in email and '.' in email.split('@')[-1]:
                break
        else:
            print("Invalid email format. Please try again.")

    while True: #telephone check
        telephone = input("Enter your Telephone number: ")
        if telephone.isdigit() and len(telephone) == 10:
            break
        else:
            print("Invalid telephone number. Please enter a 10-digit number.")

    while True : #address check
        address = input("Enter your address: ")
        if address.strip():
            break
        else:
            print("Address cannot be empty. Please try again...")

    users[username] = {
        "password": password,
        "email": email,
        "telephone": telephone,
        "address": address,
        "orders": []
    }

    with open("user.txt", "a") as file:
        file.write(f"{username} {password} {email} {telephone} {address} \n")

def load_users_from_file():
    users = {}
    try:
        with open("user.txt", "r") as file:
            for line in file:
                data = line.strip().split(' ')
                username, password, email, telephone, address = data[0], data[1], data[2], data[3], data[4]
                users[username] = {
                    "password": password,
                    "email": email,
                    "telephone": telephone,
                    "address": address,
                    "orders" : []
                }
    except FileNotFoundError:
        print("user.txt not found.")
    return users

def login():
    print(login_wp)

    global users
    users = load_users_from_file()

    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        if users[username]["password"] == password:
            print("Login Successful !")
            show_menutype(username)
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
    print(line1)

def logout():
    print("Logging out...")
    print(line1)
    main()


def show_menutype(username):
    global totalp
    menutype_id = None

    print(menutype_line)

    while menutype_id not in menutype_list and menutype_id not in ['L','E']:
        menutype_id = input("Type menu ID: ").strip().upper()

        if menutype_id not in menutype_list and menutype_id not in ['L','E']:
            print("Invalid menu ID! Please try again....")

    if menutype_id == "L":
        logout()
        return
    
    if menutype_id == "E":
        print(exit_line)
        exit()

    if menutype_id in menutype_list:
        print(line1)
        print(f"                        {menutype_list[menutype_id]} ")
        print(line1)
        print("    ID                Menu               Price")
        for item in menu_items[menutype_id]:
            print(f"    {item['ID']:<8} {item['Menu']:<24} {item['Price']:>5}")
        print(line1)
    
    menu_id = None

    while menu_id not in [item['ID'] for item in menu_items[menutype_id]]:    
        menu_id = input("Menu ID: ").strip().upper()

        if menu_id not in [item['ID'] for item in menu_items[menutype_id]]:
            print("Invalid Menu ID!! Please try again...")

    while True:
        try:
            amount = int(input("Amount: "))
            break 
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    selected_item = next((item for item in menu_items[menutype_id] if item['ID'] == menu_id), None)

    if selected_item:
        print(f"You selected {selected_item['Menu']} x{amount}")
        total_price = selected_item['Price'] * amount
        users[username]["orders"].append([selected_item['Menu'], amount, total_price])
        totalp += total_price
    print(line1)

    while True:
        nextorder = input("Next order (Y/N) or Cancel (C): ").strip().upper()

        if nextorder == 'C':
            print("Your current orders: ")
            for idx, order in enumerate(users[username]["orders"]):
                print(f"{idx + 1}: {order[0]} -Qty: {order[1]}, Price: {order[2]:.2f}")

            print(line1)

            while True:
                try:
                    cancel_index = int(input("Enter the order number to cancel: ")) - 1
                    if 0 <= cancel_index < len(users[username]["orders"]):
                        canceled_order = users[username]["orders"].pop(cancel_index)
                        totalp -= canceled_order[2]
                        print(f"Canceled: {canceled_order[0]} - Qty: {canceled_order[1]}")
                        print(line1)
                        break  
                    else:
                        print("Invalid order number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

           
            nextorder = input("Next order (Y/N): ").strip().upper()

            if nextorder == 'Y':
                show_menutype(username)
            elif nextorder == 'N':
                show_shipping_ad(username)
            else:
                print("Invalid selection. Please enter Y or N.")
                continue  

        elif nextorder == 'Y':
            show_menutype(username)
            break  
        elif nextorder == 'N':
            show_shipping_ad(username)
            break  
        else:
            print("Invalid input! Please enter Y, N, or C.")

def show_bu_card (username):
    print(line1)
    global totalp

    while True:
            member = input("BU Member Card (Y/N): ").upper()
            if member in ['Y','N']:
                break
            else:
                print("Invalid select. Please Enter Y/N")
    
    if member == 'Y':
        discount = totalp*0.2
        totalp -= discount
        print(f"Congratulations!, you got 20% discount. : {discount:.2f}")
        show_receipt(username)
    elif member == 'N':
        show_receipt(username)



def show_shipping_ad (username):
    print(shipping_line)
    user = users[username]

    print(f"Name: {username}")
    print(f"Address: {user['address']}")
    print(f"Telephone number: {user['telephone']}")


    while True:
        chang_ad = input("Chang your Address ? (Y/N): ").upper()
        if chang_ad == 'Y':
            new_ad = input("New Address: ")
            user['address'] = new_ad
            print("Change your address Successful!")
            show_bu_card(username)

        elif chang_ad == 'N':
            show_bu_card(username)

        else:
            print("Invalid select. Please Enter (Y/N)")
        print(line1)



def show_receipt(username):
    print(receipt_line)
    print("Menu                    QTY        Total Price")
    
    if len(users[username]["orders"]) == 0:
        print("No orders yet.")
        return
    
    total = 0
    for order in users[username]["orders"]:
        menu_name = order[0]
        qty = order[1]
        total_price = order[2]

        print(f"{menu_name:<24} {qty:<10} {total_price:>10.2f}")

        total += total_price
    
    print(line1)
    print(f"{'Total':<24} {'':<10} {totalp:>10.2f}")
    payment()

def payment():
    print(payment_line)
    while True:
        payment_method = input("Enter your choice (1.Credit Card / 2.Cash): ").strip()

        if payment_method == "1":
            process_credit_card()
            break
        elif payment_method == "2":
            process_cash()
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

def process_credit_card():
    global totalp
    while True:
        card_number = input("Enter your credit card number (16 digits): ")
        if len(card_number) == 16 and card_number.isdigit():
            break
        else:
            print("Invalid card number! Please enter a valid 16-digit number.")

    print(f"Total amount to be paid: {totalp:.2f} THB")
    while True:
        try:
            payment_amount = float(input("Enter the amount to pay: "))
            if payment_amount >= totalp:
                change = payment_amount - totalp
                print(f"Payment successful! Your change is: {change:.2f} THB.")
                print(end_line)
                exit()
            else:
                print("Insufficient payment! Please provide enough funds.")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

def process_cash():
    global totalp
    print(f"Total amount to be paid: {totalp:.2f} THB")
    while True:
        try:
            cash_received = float(input("Enter the amount of cash received: "))
            if cash_received >= totalp:
                change = cash_received - totalp
                print(f"Payment successful! Your change is: {change:.2f} THB.")
                print(end_line)
                exit()
            else:
                print("Insufficient amount! Please provide enough cash.")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")



def main():
    while True:
        print(wc_line)
        select_fuc = input("Select function: ")

        if select_fuc == "1":
            login()
        elif select_fuc == "2":
            register()
        elif select_fuc == "3":
            print(exit_line)
            exit()
        else:
            print("Invalid select. Please select 1, 2, or 3.")

main()