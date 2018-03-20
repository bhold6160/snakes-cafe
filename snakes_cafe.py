menu = {
    'appetizers' : ['Appetizers:','----------', 'Wings', 'Cookies', 'Spring Rolls\n'],
'entrees' : ['Entrees:', '----------','Salmon',
           'Steak', 'Meat Tornado', 'A Literal Garden\n'],
'desserts' : ['Desserts:', '----------', 'Ice Cream', 'Cake', 'Pie\n'],
'drinks' : ['Drinks', '----------', 'Coffee', 'Tea', 'Blood of the Innocent\n'],
}

user_order = []

def welcome_message():
    print('**************************************\n** Welcome to the Snakes\
Cafe! **\n** Please see our menu below. **\n** To quit at any time,\
type "quit" **\n**************************************')

class print_messages:
    def user_input(self):
        self.initial_input = input('***********************************\n** What would you\
 like to order? ''**\n***********************************\n')

    def continue_order(self):
        self.continue_order_input = input('***********************************\n** Are you finished with\
your order? Type "quit" if yes''**\n***********************************\n>')

p = print_messages()

def print_values():
    for values in menu.values():
        for value in values:
            print(value)

# def user_input():
#     initial_input = input('***********************************\n** What would you\
#  like to order? ''**\n***********************************\n')

#     continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n>')

def user_input_to_list():
    while True:
        p.continue_order
        if p.continue_order in menu.items():
            user_order.append(p.continue_order)
            print('Your current order consists of ' + str(user_order))

def user_quit():
    if p.continue_order == 'quit':
        print('***********************************\n** Your order has been completed\
        ''**\n***********************************\n')

if __name__ == "__main__":
    welcome_message()
    print_values()
    p.continue_order()
    user_input_to_list()
    user_quit()
