import uuid

menu = {
    'Appetizers': {
        'Wings': 8.00,
        'Spring Rolls': 5.00,
        'Cookies': 2.00,
        'Grilled Squid': 8.00,
        'Crab Wonton': 6.00,
        'Satay': 7.00 
    },
    'Entrees': {
        'Salmon': 15.00,
        'Steak': 20.00,
        'Meat Tornado': 25.00,
        'A Literal Garden': 12.00,
        'Pad Thai': 10.00,
        'Spicy Meatballs': 12.00 
    },
    'Desserts': {
        'Ice Cream': 6.00,
        'Cake': 6.00,
        'Pie': 7.00,
        'Mango Sicky Rice': 6.00,
        'Mushroom Yogurt': 5.00,
        'Popsicle': 3.00 
    },
    'Drinks': {
        'Coffee': 3.00,
        'Tea': 2.00,
        'Innocent Blood': 50.00,
        'Champagne': 8.00,
        'Martini': 11.00,
        'Italian Lemondrop': 10.00 
    },
    'Sides': {
        'Bread': 2.00,
        'Hot Peppers': 1.00,
        'Potatoes': 3.00,
        'Bacon': 5.00,
        'Apples': 1.00,
        'Rice': 4.00 
    }
}

user_order = {}


def welcome_message():
    welcome = print('**************************************\n\
** Welcome to the Snakes Cafe! **\n\
** Please see our menu below. **\n\
** To quit at any time, type "quit" **\n\
**************************************')
    return welcome


def print_menu():
    return_value = ''
    for key, value in menu.items():
        print('\n{}\n----------\n' .format(key))
        '''
        Input from the user for menu item
        '''
        for item, price in value.items():
            item_str = item.ljust(20)
            price_str = ('$' + str(price) + '0').rjust(15)
            new_str = item_str + price_str
            print(new_str)
            return_value += '{}: ${p:0.2f}\n' .format(item, p=price)
    return return_value


def get_user_input():
    '''
    Input from the user for menu item
    '''
    return input('***********************************\n\
** What would you like to order? ''**\n\
***********************************\n->')


def exit_program():
    exit(0)


def check_user_input():
    user_input = input('->')
    if user_input == 'quit':
        print('Order Complete')
        exit_program()
    elif user_input == 'order':
        print(print_order(user_order))
    else:
        add_order(user_input)
    return user_input


def print_order(user_order):
    order_summary = 'Order #{}\n'.format(uuid.uuid4())
    for item, quantity in user_order.items():
        item = item.title()
        for category in menu.values():
            if item in category:
                order_summary += '\n{}: {} ${}'.format(quantity, item, category[item])
    return order_summary


def add_order(item):
    for course in menu:
        if item.title() in menu[course]:
            if item in user_order:
                user_order[item] = user_order[item] + 1
            else:
                user_order[item] = 1
            print('{} has been added to your order' .format(item))
            return item


def remove_item(item):
    if item in user_order:
        user_order[item] -= 1
        if user_order[item] == 0:
            del user_order[item]
            print('{} has been removed from your order' .format(item))
        else:
            print('{} not found' .format(item))


def main():
    welcome_message()
    print_menu()

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
