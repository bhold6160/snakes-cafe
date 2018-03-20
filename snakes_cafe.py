menu = {
    'appetizers' : ['Appetizers:','----------', 'Wings', 'Cookies', 'Spring Rolls\n'],
'entrees' : ['Entrees:', '----------','Salmon',
           'Steak', 'Meat Tornado', 'A Literal Garden\n'],
'desserts' : ['Desserts:', '----------', 'Ice Cream', 'Cake', 'Pie\n'],
'drinks' : ['Drinks', '----------', 'Coffee', 'Tea', 'Blood of the Innocent\n'],
}

user_order = []

if __name__ == "__main__":
    print('**************************************\n** Welcome to the Snakes\
Cafe! **\n** Please see our menu below. **\n** To quit at any time,\
type "quit" **\n**************************************')

for key, values in menu.items():
    for value in values:
        print(value)

user_input = input('***********************************\n** What would you\
 like to order? ''**\n***********************************\n')

# continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n')

while True:
    continue_order = input('***********************************\n** Are you finished\
with your order? Type "quit" if yes''**\n***********************************\n')
    if continue_order in menu.items():
        user_order.append(continue_order)
        print('Your current order consists of ' + str(user_order))
        pass
    else:
        continue_order = 'quit()'
        print('***********************************\n** Your order has been completed\
        ''**\n***********************************\n')
        break
