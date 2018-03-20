menu = {
    'appetizers' : ['Appetizers:','----------', 'Wings', 'Cookies', 'Spring Rolls\n'],
'entrees' : ['Entrees:', '----------','Salmon',
           'Steak', 'Meat Tornado', 'A Literal Garden\n'],
'desserts' : ['Desserts:', '----------', 'Ice Cream', 'Cake', 'Pie\n'],
'drinks' : ['Drinks', '----------', 'Coffee', 'Tea', 'Blood of the Innocent\n'],
}

user_order = []

print('**************************************\n** Welcome to the Snakes\
Cafe! **\n** Please see our menu below. **\n** To quit at any time, \
type "quit" **\n**************************************')

for key, values in menu.items():
    for value in values:
        print(value)

# user_input = input('***********************************\n** What would you\
#  like to order? ''**\n***********************************\n')

# continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n')

# print(user_input)

while True:
    user_input = input('***********************************\n** What would you\
 like to order? ''**\n***********************************\n')
    if user_input in menu.items():
        user_order.append(user_input)
        print('Your current order consists of ' + str(user_order))
        pass
    else:
        user_input = 'quit()'
        print('***********************************\n** Your order has been completed\
        ''**\n***********************************\n')
        break
