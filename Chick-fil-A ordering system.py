from datetime import datetime


def main():
    # show the welcome message, set the original cost and order list, accumulate total cost and order details during the ordering process, then print a receipt
    print("-" * 76)
    print("Welcome to Chick-fil-A! Wishing you a joyful day!😄🍔🍗🥤")
    total_cost = 0
    order_details = []
    total_cost = item_order(total_cost, order_details)
    print_receipt(order_details, total_cost)

    # Process the ordering sequence for entree, drink, and side dish in order, and return the accumulated total price


def item_order(total_cost, order_details):
    total_cost = handle_entree_selection(total_cost, order_details)
    total_cost = handle_drink_selection(total_cost, order_details)
    total_cost = handle_side_selection(total_cost, order_details)
    return total_cost

    # Show the entree menu, handle the user’s choice, and compute the price


def handle_entree_selection(total_cost, order_details):
    entree_menu = show_entree_menu()
    total_cost = count_entree_cost(entree_menu, total_cost, order_details)
    return total_cost

    # Create a dictionary for the entree menu and display the menu


def show_entree_menu():
    entree_menu = {
        1: {"name": "Smokehouse BBQ Bacon Sandwich w/ Chick-fil-A Filet", "price": 8.19},
        2: {"name": "Smokehouse BBQ Bacon Sandwich w/ Grilled Filet", "price": 9.09},
        3: {"name": "Smokehouse BBQ Bacon Sandwich w/ Spicy Filet", "price": 8.49},
        4: {"name": "Chick-fil-A Chicken Sandwich", "price": 5.59},
        5: {"name": "Chick-fil-A Deluxe Sandwich", "price": 6.29},
        6: {"name": "Spicy Chicken Sandwich", "price": 5.89},
        7: {"name": "Spicy Deluxe Sandwich", "price": 6.59},
        8: {"name": "Grilled Chicken Sandwich", "price": 7.19},
        9: {"name": "Chick-fil-A Grilled Chicken Club Sandwich", "price": 9.09},
        10: {"name": "Chick-fil-A Nuggets", "price": 5.69},
        11: {"name": "Grilled Nuggets", "price": 6.45},
        12: {"name": "Chick-fil-A Chick-n-Strips", "price": 5.85},
        13: {"name": "Chick-fil-A Cool Wrap", "price": 8.75},
        14: {"name": "Spicy Cool Wrap", "price": 8.75},
        15: {"name": "Southwest Veggie Wrap", "price": 8.25},
        16: {"name": "Gluten Free Bun", "price": 1.70},
        17: {"name": "Chick-fil-A Filet", "price": 5.34},
    }
    print("-" * 76)
    print("📋🍔 Here is our entree menu:")
    for num, item in entree_menu.items():
        print(f"Press {num:<3} for {item['name']:<56} ${item['price']:>1.2f}")
    print("-" * 76)
    return entree_menu

    # Prompt the user to choose the entree number and quantity, then calculate and add the price to the total, updating the order details


def count_entree_cost(entree_menu, total_cost, order_details):
    while True:
        entree_choice_str = input("Please enter the item number you'd like to order: ").strip()
        if entree_choice_str.isdigit():
            entree_choice = int(entree_choice_str)
            if entree_choice in entree_menu:
                item = entree_menu[entree_choice]
                break
            else:
                print("Invalid input. Please enter correct item number.")
        else:
            print("Invalid input. Please enter correct item number.")
    while True:
        entree_quantity_str = input(f"🍽️You selected {item['name']}. Please enter the quantity: ").strip()
        if entree_quantity_str.isdigit():
            entree_quantity = int(entree_quantity_str)
            break
        else:
            print("Invalid input. Please enter correct item quantity.")

    # Add the selected entree’s order info to the order details list
    entree_cost = entree_quantity * item['price']
    total_cost += entree_cost
    if item['name'] and entree_quantity > 0 and entree_cost > 0:
        order_details.append({"name": item['name'], "quantity": entree_quantity, "price": entree_cost})
    print(f"You ordered {entree_quantity} x {item['name']}. Entree total: ${entree_cost:.2f}")
    print(f"Current total: ${total_cost:.2f}")
    return total_cost

    # Ask the user if they want to add a drink; if yes, display the drink menu and process the order


def handle_drink_selection(total_cost, order_details):
    drink_selection = input('Would you like to add a drink? 🥤Please enter yes or no: ').strip().lower()
    while drink_selection != "yes" and drink_selection != "no":
        print("Invalid input. Please enter yes or no.")
        drink_selection = input("Would you like to add a drink? 🥤Please enter yes or no: ").strip().lower()
    if drink_selection == "yes":
        drinks_menu = show_drinks_menu()
        total_cost = count_drinks_cost(drinks_menu, total_cost, order_details)
    return total_cost

    # Create a dictionary for the drinks menu and display the menu


def show_drinks_menu():
    drinks_menu = {
        1: {"name": "Pineapple Dragonfruit Beverage", "price": 3.65},
        2: {"name": "Freshly-Brewed Iced Tea Sweetened", "price": 2.55},
        3: {"name": "Freshly-Brewed Iced Tea Unsweetened", "price": 2.55},
        4: {"name": "Chick-fil-A Lemonade", "price": 2.95},
        5: {"name": "Chick-fil-A Diet Lemonade", "price": 2.95},
        6: {"name": "1/2 Sweet Tea 1/2 Unsweet Tea", "price": 2.55},
        7: {"name": "Sunjoy (1/2 Sweet Tea, 1/2 Lemonade)", "price": 2.95},
        8: {"name": "Sunjoy (1/2 Sweet Tea, 1/2 Diet Lemonade)", "price": 2.95},
        9: {"name": "Sunjoy (1/2 Unsweet Tea, 1/2 Lemonade)", "price": 2.95},
        10: {"name": "Sunjoy (1/2 Unsweet Tea, 1/2 Diet Lemonade)", "price": 2.95},
        11: {"name": "1/2 Lemonade 1/2 Diet Lemonade", "price": 2.95},
    }
    print("-" * 76)
    print("📋🥤 Here is our beverages menu:")
    for num, item in drinks_menu.items():
        print(f"Press {num:<3} for {item['name']:<56} ${item['price']:>1.2f}")
    print("-" * 76)
    return drinks_menu

    # Prompt the user to choose the drinks number and quantity, then calculate and add the price to the total, updating the order details


def count_drinks_cost(drinks_menu, total_cost, order_details):
    while True:
        drink_choice_str = input("Please enter the item number you'd like to order: ").strip()
        if drink_choice_str.isdigit():
            drink_choice = int(drink_choice_str)
            if drink_choice in drinks_menu:
                item = drinks_menu[drink_choice]
                break
            else:
                print("Invalid input. Please enter correct item number.")
        else:
            print("Invalid input. Please enter correct item number.")
    while True:
        drinks_quantity_str = input(f"🍽️You selected {item['name']}. Please enter the quantity: ").strip()
        if drinks_quantity_str.isdigit():
            drinks_quantity = int(drinks_quantity_str)
            break
        else:
            print("Invalid input. Please enter correct item quantity.")
    drinks_cost = drinks_quantity * item['price']
    total_cost += drinks_cost
    if item['name'] and drinks_quantity > 0 and drinks_cost > 0:
        order_details.append({"name": item['name'], "quantity": drinks_quantity, "price": drinks_cost})
    print(f"You ordered {drinks_quantity} x {item['name']}. Drinks total: ${drinks_cost:.2f}")
    print(f"Current total: ${total_cost:.2f}")
    return total_cost

    # Ask the user if they want to add a side dish; if yes, display the sides menu and process the order


def handle_side_selection(total_cost, order_details):
    side_selection = input('Would you like to add a side dish?🍟 Please enter yes or no: ').strip().lower()
    while side_selection != "yes" and side_selection != "no":
        print("Invalid input. Please enter yes or no.")
        side_selection = input("Would you like to add a side dish? 🍟Please enter yes or no: ").strip().lower()
    if side_selection == "yes":
        sides_menu = show_sides_menu()
        total_cost = count_sides_cost(sides_menu, total_cost, order_details)
    return total_cost

    # Create a dictionary for the sides menu and display the menu


def show_sides_menu():
    sides_menu = {
        1: {"name": "Chick-fil-A Waffle Potato Fries", "price": 2.79},
        2: {"name": "Fruit Cup", "price": 4.45},
        3: {"name": "Side Salad", "price": 4.49},
        4: {"name": "Mac & Cheese", "price": 4.45},
        5: {"name": "Cup of Chicken Noodle Soup", "price": 4.35},
        6: {"name": "Kale Crunch Side", "price": 4.45},
        7: {"name": "Berry Parfait", "price": 4.99},
    }
    print("-" * 76)
    print("📋🍟 Here is our sides menu:")
    for num, item in sides_menu.items():
        print(f"Press {num:<3} for {item['name']:<56} ${item['price']:>1.2f}")
    print("-" * 76)
    return sides_menu

    # Prompt the user to choose the sides number and quantity, then calculate and add the price to the total, updating the order details


def count_sides_cost(sides_menu, total_cost, order_details):
    while True:
        sides_choice_str = input("Please enter the item number you'd like to order: ").strip()
        if sides_choice_str.isdigit():
            sides_choice = int(sides_choice_str)
            if sides_choice in sides_menu:
                item = sides_menu[sides_choice]
                break
            else:
                print("Invalid input. Please enter correct item number.")
        else:
            print("Invalid input. Please enter correct item number.")
    while True:
        sides_quantity_str = input(f"🍽️You selected {item['name']}. Please enter the quantity: ").strip()
        if sides_quantity_str.isdigit():
            sides_quantity = int(sides_quantity_str)
            break
        else:
            print("Invalid input. Please enter correct item quantity.")
    sides_cost = sides_quantity * item['price']
    total_cost += sides_cost
    if item['name'] and sides_quantity > 0 and sides_cost > 0:
        order_details.append({"name": item['name'], "quantity": sides_quantity, "price": sides_cost})
    print(f"You ordered {sides_quantity} x {item['name']}. Sides total: ${sides_cost:.2f}")
    print(f"Current total: ${total_cost:.2f}")
    return total_cost

    # Print the current time, loop through each item in the order details and print the receipet information


def print_receipt(order_details, total_cost):
    print("-" * 76)
    print("📋💰 Here is the total cost:")
    print(f"{'CUSTOMER COPY':^80}")
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %I:%M:%S %p")
    print(f"{time_str:^80}")
    print("-" * 76)
    print(f"{'Item Name':<50}{'Quantity':>10}{'Price':>15}")
    print("-" * 76)
    total_items = 0
    for item in order_details:
        name = item['name']
        qty = item['quantity']
        price = item['price']
        total_items += qty
        print(f"{name:<50}{qty:>7}{'$' + format(price, '.2f'):>18}")
    print("-" * 76)
    print(f"{'Total:':<50}{total_items:>7}{'$' + format(total_cost, '.2f'):>18}")
    print(f"{'Thank you for your purchase!':^80}")
    print(f"{'We are a tax-free store — enjoy your meal😊':^80}")
    print("-" * 76)


if __name__ == "__main__":
    main()