from uuid import uuid4
import csv

menu = {
    'Appetizers': {
        'Wings': [8.00, 1],
        'Spring Rolls': [5.00, 2],
        'Cookies': [2.00, 4],
        'Grilled Squid': [8.00, 6],
        'Crab Wonton': [6.00, 8],
        'Satay': [7.00, 10],
        'Savory Tart': [10.00, 12],
        'Roasted Duck Salad': [12.00, 14],
        'Crostini Ai Funghi': [13.00, 16],
        'Lobster Ravioli': [17.00, 18],
        'Oysters': [15.00, 20],
        'Bagna Cauda': [14.00, 22]
    },
    'Entrees': {
        'Salmon': [15.00, 0],
        'Steak': [20.00, 1],
        'Meat Tornado': [25.00, 1],
        'A Literal Garden': [12.00, 3],
        'Pad Thai': [10.00, 5],
        'Spicy Meatballs': [12.00, 8],
        'Andouille Hash': [15.00, 21],
        'Toulouse Beignets': [15.00, 34],
        'Dutch Baby': [10.00, 55],
        'Lamb Sliders': [17.00, 89],
        'Crab Nachos': [21.00, 144],
        'Chicken Parmesan': [19.00, 233]
    },
    'Desserts': {
        'Ice Cream': [6.00, 377],
        'Cake': [6.00, 610],
        'Pie': [7.00, 987],
        'Mango Sicky Rice': [6.00, 1597],
        'Mushroom Yogurt': [5.00, 2584],
        'Popsicle': [3.00, 4181],
        'Butterfinger': [6.00, 6765],
        'Banana Split': [7.00, 10946],
        'Red Velvet Cake': [8.00, 17711],
        'Chocolate Truffle': [8.00, 28657],
        'Chocolate Fudge Cake': [8.00, 46368],
        'Cheesecake': [8.00, 75025]
    },
    'Drinks': {
        'Coffee': [3.00, 1],
        'Tea': [2.00, 3],
        'Innocent Blood': [50.00, 5],
        'Champagne': [8.00, 7],
        'Martini': [11.00, 9],
        'Italian Lemondrop': [10.00, 11],
        'Pitcher of beer': [10.00, 13],
        'Regret': [15.00, 15],
        'Dark And Stormy': [11.00, 17],
        'Greek Martini': [12.5, 19],
        'White Wine': [12.00, 21],
        'Red Wine': [12.00, 23]
    },
    'Sides': {
        'Bread': [2.00, 25],
        'Hot Peppers': [1.00, 27],
        'Potatoes': [3.00, 29],
        'Bacon': [5.00, 31],
        'Apples': [1.00, 33],
        'Rice': [4.00, 35],
        'Noodles': [4.00, 37],
        'Eggs': [3.00, 39],
        'Corn': [4.00, 41],
        'Waffles': [6.00, 43],
        'Onions': [2.00, 45],
        'Chickpeas': [4.00, 47]
    }
}

basket = {}
tax = .101

def welcome_message():
    """
    Prints the welcome message to the user
    """
    print("""
************************************\n\
- Welcome to the Snakes Cafe!\n\
- Please see our menu below.\n\
- Remove an item type "remove"<item>\n\
- Type "menu" anytime to view our menu\n\
- Type "order" to complete your order\n\
- Quit at any time, type "q"\n\
************************************""")

def print_menu():
    """
    Prints the menu to the user
    """
    return_value = ''
    for key, value in menu.items():
        print('\n{}\n-----------------------------------\n' .format(key))
        for item, price in value.items():
            price = price[0]
            # import pdb; pdb.set_trace()
            item_str = item.ljust(20)
            price_str = ('$' + str(price) + '0').rjust(15)
            new_str = item_str + price_str
            print(new_str)
            return_value += '{}: ${}\n' .format(item, price)
    return return_value


def get_user_input():
    """
    Message to the user
    """
    print("""
***********************************\n\
** What would you like to order?**\n\
***********************************""")


def exit_program():
    """
    Will exit program when called
    """
    exit(0)


def check_user_input(menu):
    """
    Prompts user for input and listens for input
    """
    menu = menu.items()
    user_input = input('->')
    if user_input == 'q':
        user_quit()
    elif user_input == 'order':
        place_order()
    elif user_input.startswith('remove'):
        removed_item = user_input.split(' ')[-1]
        remove_item(removed_item)
    elif user_input == 'menu':
        print_menu()
    elif user_input.title() in menu:
        item_category(user_input)
    # elif user_input != menu:
    #     print('Not on the Menu. Try again...')
    else:
        user_input = user_input.split(' ')
        if len(user_input) == 1:
            add_order(user_input)
        else:
            add_order(user_input[0], user_input[1])
    return user_input


def user_quit():
    """
    Exits the program
    """
    print('Come back soon!')
    exit_program()


def place_order():
    """
    Printing out the users finished order
    """
    print('Order #{}'.format(uuid4()))
    print(print_order(basket))



def item_category(category):
    """
    Retrieves categories from the dictionary and prints them to the user
    """
    category = category.title()
    for key in menu[category]:
        print(key)


def print_order(user_order):
    """
    Prints order when user is finished selecting items
    """
    sub_total = calculate_total()
    order_tax_total = calculate_tax()
    final_total = order_tax_total + sub_total
    order_summary = ' '
    for item, quantity in user_order.items():
        item = item.title()
        for category in menu.values():
            if item in category:
                order_summary += '\n{}: {} ${:0.2f}'.format(quantity, item, category[item])
    order_summary += '\nSubtotal: ${:0.2f}'.format(sub_total)
    order_summary += '\nTax: ${t:0.2f}'.format(t = order_tax_total)
    order_summary += '\nTotal: ${h:0.2f}'.format(h = final_total)
    return order_summary


def calculate_total():
    """
    Calculating returning to the total number of items multiplied by their quantity
    """
    order_total = 0
    for item, quantity in basket.items():
        item = item.title()
        for category in menu.values():
            if item in category:
                item_price = category[item] * quantity
                order_total += item_price
    return order_total


def calculate_tax():
    """
    Calculating the tax by multiplying it by our total
    """
    tax_total = calculate_total() * tax
    return tax_total


def add_order(item, quantity=1):
    """
    Adds items to users total order
    """
    for course in menu:
        if type(item) == list:
            item = item[0]
        item = item.title()
        if item in menu[course]:
            if item in basket:
                basket[item] = basket[item] + int(quantity)
                print('{} {} added to your order'.format(basket[item], item))
            else:
                basket[item] = 1
                print('{} added to your order' .format(item))

            return item


def remove_item(item):
    """
    Will remove items when called
    """
    item = item.title()
    if item in basket:
        basket[item] -= 1
        if basket[item] == 0:
            del basket[item]
        print('{} has been removed from your order' .format(item))
    else:
        print('{} not found' .format(item))


def optional_menu():
    """
    Presents the user with an prompt to enter in their own menu
    """
    menu_name = input('Please enter your menu file path: ')
    new_menu = {}
    with open(menu_name) as csv_file:
        filename = csv.reader(csv_file)
        for row in filename:
            category, item, price, quantity = row
            if category in new_menu:
                new_menu[category][item] = float(price)
            else:
                new_menu[category] = {item:float(price)}
        print(new_menu)
        

def main():
    """
    Main entry point for the app 
    """
    welcome_message()
    print_menu()
    get_user_input()

    while True:
        user_input = check_user_input(menu)
        if user_input is None:
            print('Not on the Menu. Try again...')
            continue


if __name__ == "__main__":
    # optional_menu()
    try:
        main()
    except KeyboardInterrupt:
        pass
