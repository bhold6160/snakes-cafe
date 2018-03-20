appetizers = ['Appetizers:\n','----------', 'Wings', 'Cookies', 'Spring Rolls\n']
entrees = ['Entrees:', '----------','Salmon',
           'Steak', 'Meat Tornado', 'A Literal Garden\n']
desserts = ['Desserts:', '----------', 'Ice Cream', 'Cake', 'Pie\n']
drinks = ['Drinks', '----------', 'Coffee', 'Tea', 'Blood of the Innocent\n']

user_order = []
print('**************************************\n** Welcome to the Snakes\
Cafe! **\n** Please see our menu below. **\n** To quit at any time, \
type "quit" **\n**************************************')

for item in appetizers:
    print(item)

for item in entrees:
    print(item)

for item in desserts:
    print(item)

for item in drinks:
    print(item)

user_quit = 'quit()'
while True:
    user_input = input('***********************************\n** What would you like to order? '
                       '**\n***********************************\n')
    if user_input in drinks or user_input in desserts or user_input in entrees or user_input in appetizers:
        user_order.append(user_input)
        print('Your current order consists of ' + str(user_order))
        continue
    else:
        user_input = user_quit
        break