cart = []
# colour codes (Glenda)
TBLACK = '\033[30;1m'
TGREEN = '\033[32m'
TBLUE = '\033[34m'
TCYAN = '\033[36;1m'
TPURPLE = '\033[35;1m'
TYELLOW = '\033[33m'
TDEFAULT = '\033[m'
TBRIGHTYELLOW = '\033[93m'
TBRIGHTRED = '\033[91m'
TBRIGHTPURPLE = '\033[95m'
TBRIGHTBLUE = '\033[94m'
TBRIGHTGREEN = '\033[92m'

# dictionary of items (Glenda)
items = {
    'N32': ['Drinks(CD10)', 'Neo’s Green Tea', '$3.00'],
    'M13': ['Drinks(CD10)', 'Melo Chocolate Malt Drink', '$2.85'],
    'V76': ['Drinks(CD10)', 'Very-Fair Full Cream Milk', '$3.50'],
    'N14': ['Drinks(CD10)', 'Nirigold UHT Milk', '$4.15'],
    'L11': ['Beer(CB20)', 'Lion (24 x 320 ml)', '$52.0'],
    'P21': ['Beer(CB20)', 'Panda (24 x 320 ml)', '$78.0'],
    'A54': ['Beer(CB20)', 'Axe (24 x 320 ml)', '$58.0'],
    'H91': ['Beer(CB20)', 'Henekan (24 x 320 ml)', '$68.0'],
    'E11': ['Frozen(CF30)', 'Edker Ristorante Pizza 355g', '$6.95'],
    'F43': ['Frozen(CF30)', 'Fazzler Frozen Soup 500g', '$5.15'],
    'CP31': ['Frozen(CF30)', 'CP Frozen Ready Meal 250g', '$4.12'],
    'D72': ['Frozen(CF30)', 'Duitoni Cheese 270g', '$5.60'],
    'FP76': ['Household(CH40)', 'FP Facial Tissues', '$9.50'],
    'FP32': ['Household(CH40)', 'FP Premium Kitchen Towel', '$5.85'],
    'K22': ['Household(CH40)', 'Klinex Toilet Tissue Rolls', '$7.50'],
    'D14': ['Household(CH40)', 'Danny Softener', '$9.85'],
    'SS93': ['Snacks(CS50)', 'Singshort Seaweed', '$3.10'],
    'MC14': ['Snacks(CS50)', 'Mei Crab Cracker', '$2.05'],
    'R35': ['Snacks(CS50)', 'Reo Pokemon Cookie', '$4.80'],
    'HS11': ['Snacks(CS50)', 'Huat Seng Crackers', '$3.55'],
}
# dictionary for user to select item ( user-friendly) - Li Qing
category_items = {
    "d": [('N32', 'Neo’s Green Tea'), ('M13', 'Melo Chocolate Malt Drink'), ('V76', 'Very-Fair Full Cream Milk'), ('N14', 'Nirigold UHT Milk')],
    "b": [('L11', 'Lion (24 x 320 ml)'), ('P21', 'Panda (24 x 320 ml)'), ('A54', 'Axe (24 x 320 ml)'), ('H91', 'Henekan (24 x 320 ml)')],
    "f": [('E11', 'Edker Ristorante Pizza 355g'), ('F43', 'Fazzler Frozen Soup 500g'), ('CP31', 'CP Frozen Ready Meal 250g'), ('D72', 'Duitoni Cheese 270g')],
    "h": [('FP76', 'FP Facial Tissues'), ('FP32', 'FP Premium Kitchen Towel'), ('K22', 'Klinex Toilet Tissue Rolls'), ('D14', 'Danny Softener')],
    "s": [('SS93', 'Singshort Seaweed'), ('MC14', 'Mei Crab Cracker'), ('R35', 'Reo Pokemon Cookie'), ('HS11', 'Huat Seng Crackers')]
}


def display_products():  # Li Qing
    print(TBLUE + f"| {f'{"Category":<16s} | {"Item":<28s} | {"Code":<5s} | {"Price":<6s}':40} |")  # text is blue colour

    for key, value in items.items():
        category = value[0]
        item = value[1]
        code = key
        price = value[2]
        print(TCYAN + f"| {f'{category:<16s} | {item:<28s} | {code:<5s} | {price:<6s}':40s} |")


def place_order():  # Li Qing
    choices = "d f b h s".split()

    display_products()  # display the categories
    print("Categories:")
    print("\tD or d(rinks)")
    print("\tF or f(rozen)")
    print("\tB or b(eer)")
    print("\tH or h(ousehold)")
    print("\tS or s(nacks)")
    print(TDEFAULT)   # change back to default colour

    while True:   # Li Qing
        category_choice = input("Please enter the initial of the category you are keen on:  ").lower()
        if category_choice.lower() not in choices:
            print(TBRIGHTRED + "Please enter the correct category")
            print(TDEFAULT)  # change back to default colour
            continue

        break

    print()
    for idx, item in enumerate(category_items[category_choice.lower()]):  # Glenda
        code = item[0]
        name = item[1]
        print(TBLUE + f"{idx + 1:>2d}. {name} ({items[code][2]})")  # text is blue colour
    while True:
        print(TDEFAULT)   # change back to default colour
        selection_choice = input("Enter your choice (enter 1-4): ")
        try:
            selection_choice = int(selection_choice)
        except ValueError:
            print(TBRIGHTRED + "Please select a choice")
            continue

        if 1 <= selection_choice <= 4:
            selected_code = category_items[category_choice][selection_choice - 1][0]
            break

        print(TBRIGHTRED + "Please select a choice")  # text is bright red colour

    while True:
        quantity = input("Enter the quantity: ")
        try:
            quantity = int(quantity)
        except ValueError:
            print(TBRIGHTRED + "Please enter a number")
            print(TDEFAULT)  # change back to default colour
            continue

        if quantity <= 0:
            print(TBRIGHTRED + "Please enter a positive quantity")
            print(TDEFAULT)  # change back to default colour
            continue

        cart.append([items[selected_code][1], items[selected_code][2], quantity])
        print(TGREEN + "Selected added to cart.")    # text is green colour
        break


def view_cart():   # Shreya
    if not cart:   # if there is nothing in the cart it will print out cart is empty
        print("Cart is empty.")
        return

    for item in cart:
        name = item[0]
        price = item[1]
        quantity = item[2]
        print(TYELLOW + f"{name} (x{quantity}) - {price} each ")  # text is yellow colour


def remove_cart():  # Shreya
    if not cart:
        print("Cart is empty.")
        return

    for idx, item in enumerate(cart):
        name = item[0]
        price = item[1]
        quantity = item[2]
        print(TYELLOW + f"{idx + 1:>2d}. {name} (x{quantity}) - {price}/each")  # text is yellow colour

    while True:
        print(TDEFAULT)  # change back to default colour
        choice = input("Enter your choice (or leave empty to finish): ")
        if choice.strip() == "":
            return

        try:
            choice = int(choice)
        except ValueError:
            print(TBRIGHTRED + "Please enter a number")
            print(TDEFAULT)  # change back to default colour
            continue

        if choice <= 0 or choice > len(cart):  # if user did not choose the correct choices
            print(TBRIGHTRED + "Please enter a valid number from the cart")
            print(TDEFAULT)  # change back to default colour
            continue

        while True:
            new_quantity = input(f"Enter a new quantity for {cart[choice - 1][0]} (0 to remove item): ")

            try:
                new_quantity = int(new_quantity)
            except ValueError:
                print(TBRIGHTRED + "Please enter a valid number")
                print(TDEFAULT)  # change back to default colour
                continue

            if new_quantity < 0:
                print(TBRIGHTRED + "Please enter a positive number for quantity")
                print(TDEFAULT)  # change back to default colour
                continue

            if new_quantity == 0:
                cart.pop(choice - 1)
            else:
                cart[choice - 1][2] = new_quantity
            break


def checkout():   # Glenda and Li Qing
    if not cart:  # if there is nothing in the cart
        print("Cart is empty.")
        return
    # Glenda (formating discounts)
    print(TPURPLE + f"| {f'{"Type of Discount":<20s} | {'Discount':>10s}':30s} |")
    print(TPURPLE + f"| {f'{"Seniors":<20s} | {'10%':>10s}':30s} |")
    print(TPURPLE + f"| {f'{"Members":<20s} | {'8%':>10s}':30s} |")
    print(TPURPLE + f"| {f'{"NSMen":<20s} | {'5%':>10s}':30s} |")
    print(TDEFAULT)  # change back to default colour

    # Li Qing
    discount_rate = 0
    discount_name = ""

    while True:
        choice = input("Do you fall under the following categories? (y/n): ")
        choice = choice.lower()

        if choice not in "y n".split():
            print(TBRIGHTRED + "Please enter either y(es) or n(o)")
            print(TDEFAULT)  # change back to default colour
            continue

        break

    if choice == "y":
        while True:
            print(TPURPLE + "1. Seniors")
            print(TPURPLE + "2. Members")
            print(TPURPLE + "3. NSMen")
            print(TDEFAULT)  # change back to default colour

            choice = input("Enter the category you fall under: ")
            try:
                choice = int(choice)
            except ValueError:
                print(TBRIGHTRED + "Please enter a valid choice")
                print(TDEFAULT)  # change back to default colour
                continue

            if choice not in [1, 2, 3]:
                print(TBRIGHTRED + "Please enter a valid choice")
                print(TDEFAULT)  # change back to default colour
                continue

            if choice == 1:
                discount_rate = 0.10
                discount_name = "Senior Discount (10%)"
            elif choice == 2:
                discount_rate = 0.08
                discount_name = "Members Discount (8%)"
            elif choice == 3:
                discount_rate = 0.05
                discount_name = "NSMen Discount (5%)"
            else:
                discount_rate = 0

            break

    total = 0
    subtotal = 0
    gst = 0.09

    for item in cart:
        price = item[1]
        quantity = item[2]

        price = float(price.replace("$", ""))
        subtotal += price * quantity

    discount = subtotal * discount_rate
    derived_gst = subtotal * gst
    total = subtotal - discount + derived_gst

    print(TGREEN + f"| {f'{"*" * 35} Receipt {"*" * 35}':80s} |")   # TGREEN - colour code
    print(TGREEN + f'| {f"{'Item':<30s} {'Qty':>5s} {'Price':>10s} {'Total':>15s}":80s} |')

    for item in cart:
        name = item[0]
        price = item[1]
        quantity = item[2]

        price = float(price.replace("$", ""))
        item_total = price * quantity

        print(TGREEN + f'| {f"{name:<30s} {quantity:>5d} {price:>10.2f} {item_total:>15.2f}":80s} |')

    print(TGREEN + f"| {"-" * 80} |")
    print(TGREEN + f'| {f"{'Total Price (before discount and GST)':<47} {subtotal:>15.2f}":80s} |')

    if discount_rate > 0:
        print(TGREEN + f'| {f"{discount_name:<47} {discount:>15.2f}":80s} |')

    print(TGREEN + f"| {"-" * 80} |")
    print(TGREEN + f'| {f"{'GST (9%)':<47} {derived_gst:>15.2f}":80s} |')
    print(TGREEN + f'| {f"{'Total':<47} {total:>15.2f}":80s} |')
    print(TGREEN + "|--------------------------------------Thank You-----------------------------------|")
    print(TGREEN + "                                                                                    ")

    cart.clear()  # cart clears for user to make a separate purchase if they were to forget any items


# Glenda , Li Qing , Shreya
def main():
    print(TCYAN + "+----+----+---- Menu ----+----+----+")
    print(TPURPLE + "| 1. View Menu/Place Orders        |")
    print(TPURPLE + "+ 2. View Cart                     +")
    print(TPURPLE + "| 3. Remove Existing Orders        |")
    print(TPURPLE + "+ 4. Payment/Checkout              +")
    print(TPURPLE + "| 5. Exit                          |")
    print(TCYAN + "+----+----+----+----+----+----+----+")
    print(TDEFAULT)    # change back to default colour

    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            break
        except ValueError:
            print(TBRIGHTRED + "Please put a valid choice")
            print(TDEFAULT)  # change back to default colour
            continue

    if choice == 1:
        place_order()
        main()
    elif choice == 2:
        view_cart()
        main()
    elif choice == 3:
        remove_cart()
        main()
    elif choice == 4:
        checkout()
        main()
    elif choice == 5:
        def print_thank_you():   # text will be yellow colour (Glenda , Li Qing , Shreya)
            message = TBRIGHTYELLOW + """  
                ,--------.,--.                     ,--.                                    ,---.                             
                '--.  .--'|  ,---.  ,--,--.,--,--, |  |,-.     ,--. ,--.,---. ,--.,--.    |  .-' ,---. ,--.--.               
                   |  |   |  .-.  |' ,-.  ||      \\|     /      \\  '  /| .-. ||  ||  |    |  `-,| .-. ||  .--'               
                   |  |   |  | |  |\\ '-'  ||  ||  ||  \\  \\       \\   ' ' '-' ''  ''  '    |  .-'' '-' '|  |                  
                   `--'   `--' ---' `--'--''--'---''--'`--'    /    /   `----'  `--'`-'   `-'   `---' '--'
               ,--.                          ,--.              `---'             ,--.   ,--.    ,--.                       
         ,---. |  ,---.  ,---.  ,---.  ,---. --' ,--,--,  ,---.     ,--.   ,---.  --'  ,-  '-.  |  ,---.       ,--., ,--. ,----.  
        (  .-' |  .-.  || .-. || .-. || .-. |,--.|| ._. | .-. ||    |   |  |   | .- -. '-| |.-' |   .-.  |     |   | |  | (  .-'
        .-'  `)|  | |  |' '-' '| '-' '| '-' '|  ||  ||  |' '-' '    |   .'.|   | |   |   | |    |  |   | |     '   ' |  | .---' )
        ----' `--' `--' `---' |  |-' |  |-' --'--''--'.-   __| |    '-''--'----' '---'   '--'   '--'   '-'     '---''---' `----'
                               `--'   `--'                `----'                                                 

            ,_     _                                  ,_     _
            |\\_,-~/                                   |\\_,-~/
            / _  _ |    ,--.                          / _  _ |    ,--.
            (   .   )   / ,-'                         (   -   )   / ,-'
            \\  _T_/-._( (                             \\  _T_/-._( (
            /         `. \\                            /         `. \\
            |        _  \\ |                           |        _  \\ |
            \\ \\ ,  /      |                           \\ \\ ,  /      |
             || |-_\\__   /                             || |-_\\__   /
            ((_/`(____,-                               ((_/`(____,-
          """

            print(message)

        print_thank_you()

    else:
        print("Please enter a valid choice")
        main()


if __name__ == '__main__':
    main()
