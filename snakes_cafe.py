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

def get_user_input():
    return input('***********************************\n\
** What would you like to order? ''**\n\
***********************************\n>')


def print_menu():
    return_value = ''
    for value in menu.values():
        for item, price in value.items():
            print('{}: {}' .format(item, price))
            return_value += '{}: {}\n' .format(item, price)
    return return_value

#     continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n>')

def user_input_to_list():
    while True: 
        user_input = get_user_input()
        # import pdb; pdb.set_trace()
        for item in menu:
            if user_input in item:
                user_order.append(user_input)
    return user_order

def exit_program():
    exit(0)

def check_user_input(guess, answer):
    if guess == 'quit':
        exit_program()
    return guess == answer


def response(output):
    '''Doc strings are good'''
    if output is True:
        return '''
        ***********************************\n\
        ** Are you finished with your order? Type "quit" if yes''**\n\
        ***********************************\n>
        '''
    return 'Try Again...'


def main():
    '''
    Main function which acts as an entry point to the application when run as a script
    '''
    welcome_message()
    print_menu()

    while True:
        user_input = get_user_input()
        try:
            output = check_user_input(user_input, menu.values())
        except TypeError:
            print(response(False))

        if output is True:
            print(response(output))
            break


if __name__ == "__main__":
    main()
    # user_input_to_list()
