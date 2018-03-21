# menu = {
#     'appetizers' : ['Appetizers:','----------', 'Wings', 'Cookies', 'Spring Rolls\n'],
# 'entrees' : ['Entrees:', '----------','Salmon',
#            'Steak', 'Meat Tornado', 'A Literal Garden\n'],
# 'desserts' : ['Desserts:', '----------', 'Ice Cream', 'Cake', 'Pie\n'],
# 'drinks' : ['Drinks', '----------', 'Coffee', 'Tea', 'Blood of the Innocent\n'],
# }

menu = {
    'appetizers': {'Wings': 8.00, 'Spring Rolls': 5.00, 'Cookies': 2.00},
    'entrees': {'Salmon': 15.00, 'Steak': 20.00, 'Meat Tornado': 25.00, 'A Literal Garden': 12.00},
    'desserts': {'Ice Cream': 6.00, 'Cake': 6.00, 'Pie': 7.00},
    'drinks': {'Coffee': 3.00, 'Tea': 2.00, 'Blood of the Innocent': 50.00}
}

user_order = []

def welcome_message():
    print('**************************************\n** Welcome to the Snakes\
Cafe! **\n** Please see our menu below. **\n** To quit at any time,\
type "quit" **\n**************************************')


def first_input():
    initial_input = input('***********************************\n** What would you\
 like to order? ''**\n***********************************\n>')
    return initial_input

#     def continue_order(self):
#         self.continue_order_input = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n>')

def print_menu():
    return_value = ''
    for value in menu.values():
        for item, price in value.items():
            print('{}: {}' .format(item, price))
            return_value += '{}: {}\n' .format(item, price)
    return return_value

# def user_input():
#     initial_input = input('***********************************\n** What would you\
#  like to order? ''**\n***********************************\n')

#     continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n>')

def user_input_to_list():
    while True: 
        user_input = first_input()
        # import pdb; pdb.set_trace()
        for item in menu:
            if user_input in item:
                user_order.append(user_input)
                print('Your current order consists of ' + str(user_order))

# def user_quit():
#     if  == 'quit':
#         print('***********************************\n** Your order has been completed\
#         ''**\n***********************************\n')

if __name__ == "__main__":
    welcome_message()
    print_menu()
    user_input_to_list()
    # user_quit()
