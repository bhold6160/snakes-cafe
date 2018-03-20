menu = {
    'appetizers': {'Wings': 8.00, 'Spring Rolls': 5.00, 'Cookies': 2.00},
    'entrees': {'Salmon': 15.00, 'Steak': 20.00, 'Meat Tornado': 25.00, 'A Literal Garden': 12.00},
    'desserts': {'Ice Cream': 6.00, 'Cake': 6.00, 'Pie': 7.00},
    'drinks': {'Coffee': 3.00, 'Tea': 2.00, 'Blood of the Innocent': 50.00}
}

user_order = []



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

if __name__ == "__main__":
    print('**************************************\n** Welcome to the Snakes\
    Cafe! **\n** Please see our menu below. **\n** To quit at any time,\
    type "quit" **\n**************************************')