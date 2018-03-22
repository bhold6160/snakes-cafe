import uuid

menu = {
    'appetizers': {
        'Wings': [8.00, 0],
        'Spring Rolls': [5.00, 0],
        'Cookies': [2.00, 0],
        'Grilled Squid': [8.00, 0],
        'Crab Wonton': [6.00, 0],
        'Satay': [7.00, 0]
    },
    'entrees': {
        'Salmon': [15.00, 0],
        'Steak': [20.00, 0],
        'Meat Tornado': [25.00, 0],
        'A Literal Garden': [12.00, 0],
        'Pad Thai': [10.00, 0],
        'Spicy Meatballs': [12.00, 0]
    },
    'desserts': {
        'Ice Cream': [6.00, 0],
        'Cake': [6.00, 0],
        'Pie': [7.00, 0],
        'Mango with Sicky Rice': [6.00, 0],
        'Mushroom Yogurt': [5.00, 0],
        'Popsicle': [3.00, 0]
    },
    'drinks': {
        'Coffee': [3.00, 0],
        'Tea': [2.00, 0],
        'Blood of the Innocent': [50.00, 0],
        'Champagne': [8.00, 0],
        'Martini': [11.00, 0],
        'Italian Lemondrop': [10.00, 0]
    },
    'sides': {
        'Bread': [2.00, 0],
        'Hot Peppers': [1.00, 0],
        'Potatoes': [3.00, 0],
        'Bacon': [5.00, 0],
        'Apples': [1.00, 0],
        'Rice': [4.00, 0]
    }
}

user_order = []


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
        for item, price in value.items():
            item_str = item.ljust(20)
            price_str = ('$' + str(price[0]) + '0').rjust(15)
            new_str = item_str + price_str
            print(new_str)
            return_value += '{}: ${p:0.2f}\n' .format(item, p=price[0])
    return return_value


def get_user_input():
    return input('***********************************\n\
** What would you like to order? ''**\n\
***********************************\n>')


def exit_program():
    exit(0)


def check_user_input(guess, answers):
    if guess == 'quit':
        exit_program()
    for answer in answers:
        if guess in answer:
            return True

def print_order():
    order_summary = 'Order #{}\n'.format(uuid.uuid4())
    for item in user_order:
        order_summary += str(user_order)
        return order_summary


# def response(output):
#     '''
#     Checking user input 
#     '''
#     if output is True:
#         check_order_complete = input('\
# ***********************************\n\
# ** Are you finished with your order? Type "quit" if yes''**\n\
# ***********************************\n>')
#     if check_order_complete == 'quit':
#         return True
#     else:
#         return 'Try again...'


def main():
    '''
    Main function which is our entry point to the application when run
    '''
    welcome_message()
    print_menu()

    while True:
        user_input = get_user_input()
        user_output = check_user_input(user_input, menu.values())
        if user_output is None:
            print('Not on the Menu. Try again...')
            continue
        user_order.append(user_input)
        print(print_order())

if __name__ == "__main__":
    main()
