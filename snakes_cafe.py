import uuid

menu = {
    'appetizers': {
        'Wings': 8.00,
        'Spring Rolls': 5.00,
        'Cookies': 2.00,
        'Grilled Squid': 8.00,
        'Crab Wonton': 6.00,
        'Satay': 7.00
    },
    'entrees': {
        'Salmon': 15.00,
        'Steak': 20.00,
        'Meat Tornado': 25.00,
        'A Literal Garden': 12.00,
        'Pad Thai': 10.00,
        'Spicy Meatballs': 12.00
    },
    'desserts': {
        'Ice Cream': 6.00,
        'Cake': 6.00,
        'Pie': 7.00,
        'Mango with Sicky Rice': 6.00,
        'Mushroom Yogurt': 5.00,
        'Popsicle': 3.00
    },
    'drinks': {
        'Coffee': 3.00,
        'Tea': 2.00,
        'Blood of the Innocent': 50.00,
        'Champagne': 8.00,
        'Martini': 11.00,
        'Italian Lemondrop': 10.00
    },
    'sides': {
        'Bread': 2.00,
        'Hot Peppers': 1.00,
        'Potatoes': 3.00,
        'Bacon': 5.00,
        'Apples': 1.00,
        'Rice': 4.00}
}

user_order = []

def welcome_message():
    welcome = print('**************************************\n\
** Welcome to the Snakes Cafe! **\n\
** Please see our menu below. **\n\
** To quit at any time, type "quit" **\n\
**************************************')
    return welcome

def first_input():
    initial_input = input('***********************************\n\
** What would you like to order? ''**\n\
***********************************\n>')
    return initial_input

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
        user_input = first_input()
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

# def user_quit():
#     quit_return = 'quit()'
#     user_input = first_input
#     if user_input == 'quit':
#         print('***********************************\n** Your order has been completed\
#         ''**\n***********************************\n')
#         return quit_return

if __name__ == "__main__":
    welcome_message()
    print_menu()
    user_input_to_list()
    # user_quit()
