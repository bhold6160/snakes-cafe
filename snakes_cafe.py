from uuid import uuid4
import csv

menu = {
    'Appetizers': {
        'Wings': 8.00,
        'Spring Rolls': 5.00,
        'Cookies': 2.00,
        'Grilled Squid': 8.00,
        'Crab Wonton': 6.00,
        'Satay': 7.00,
        'Savory Tart': 10.00,
        'Roasted Duck Salad': 12.00,
        'Crostini Ai Funghi': 13.00,
        'Lobster Raviolo Deconstructed': 17.00,
        'Fresh Northwest Oysters': 15.00,
        'Bagna Cauda': 14.00
    },
    'Entrees': {
        'Salmon': 15.00,
        'Steak': 20.00,
        'Meat Tornado': 25.00,
        'A Literal Garden': 12.00,
        'Pad Thai': 10.00,
        'Spicy Meatballs': 12.00,
        'Spicy Creole Andouille Hash': 15.00,
        'Toulouse Beignets': 15.00,
        'Dutch Baby': 10.00,
        'Lamb Sliders': 17.00,
        'Crab Nachos': 21.00,
        'Chicken Parmesan': 19.00
    },
    'Desserts': {
        'Ice Cream': 6.00,
        'Cake': 6.00,
        'Pie': 7.00,
        'Mango Sicky Rice': 6.00,
        'Mushroom Yogurt': 5.00,
        'Popsicle': 3.00,
        'Butterfinger Cheesecake': 6.00,
        'Banana Split': 7.00,
        'Red Velvet Cake': 8.00,
        'Chocolate Truffle': 8.00,
        'Chocolate Fudge Cake': 8.00,
        'Bailey\'s Irish Cream Cheesecake': 8.00
    },
    'Drinks': {
        'Coffee': 3.00,
        'Tea': 2.00,
        'Innocent Blood': 50.00,
        'Champagne': 8.00,
        'Martini': 11.00,
        'Italian Lemondrop': 10.00,
        'Pitcher And Catcher': 10.00,
        'Regret': 15.00,
        'Dark And Stormy': 11.00,
        'Greek Martini': 12.5,
        'White Wine': 12.00,
        'Red Wine': 12.00
    },
    'Sides': {
        'Bread': 2.00,
        'Hot Peppers': 1.00,
        'Potatoes': 3.00,
        'Bacon': 5.00,
        'Apples': 1.00,
        'Rice': 4.00,
        'Noodles': 4.00,
        'Eggs': 3.00,
        'Corn': 4.00,
        'Waffles': 6.00,
        'Onions': 2.00,
        'Chickpeas': 4.00
    }
}

basket = {}
tax = .101

def welcome_message():
    """
    Prints the welcome message to the user
    """
    welcome = print('**************************************\n\
** Welcome to the Snakes Cafe! **\n\
** Please see our menu below. **\n\
** To quit at any time, type "quit" **\n\
**************************************')
    return welcome


def print_menu():
    """
    Prints the menu to the user
    """
    return_value = ''
    for key, value in menu.items():

        print('\n{}\n--------------------------------------\n' .format(key))
        for item, price in value.items():
            item_str = item.ljust(20)
            price_str = ('$' + str(price) + '0').rjust(15)
            new_str = item_str + price_str
            print(new_str)
            return_value += '{}: ${p:0.2f}\n' .format(item, p=price)
    return return_value


def get_user_input():
    """
    Input from the user for menu item
    """
    print('***********************************\n\
** What would you like to order? ''**\n\
***********************************')


def exit_program():
    """
    Will exit program when called
    """
    exit(0)


def check_user_input():
    """
    Prompts user for input and listens for input
    """
    user_input = input('->')
    import pdb; pdb.set_trace()
    if user_input == 'quit':
        user_quit()
    elif user_input == 'order':
        place_order()
    elif user_input.startswith('remove'):
        removed_item = user_input.split(' ')[-1]
        remove_item(removed_item)
    elif user_input == 'menu':
        print_menu()
    elif user_input.title() in menu:
        categories_items(user_input)
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
<<<<<<< HEAD
    '''
    # print('Order #{}'.format(uuid4()))
=======
    """
    print('Order #{}\n'.format(uuid4()))
>>>>>>> 541ffbfe9c99e831ced1480b7594632c9216ebb6
    print(print_order(basket))



def categories_items(category):
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
                print('{} {} has been added to your order'.format(basket[item], item))
            else:
                basket[item] = 1
                print('{} has been added to your order' .format(item))

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


# def optional_menu():

#     menu_name = input('Please enter your menu name: ').strip()
#     try:
#         with open as csvfile


def main():
    """
    Main entry point for the app 
    """
    welcome_message()
    print_menu()
    get_user_input()

    while True:
        user_input = check_user_input()
        if user_input is None:
            print('Not on the Menu. Try again...')
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
