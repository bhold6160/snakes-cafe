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

for key, value in menu.items():
    for item, price in value.items():
        print(item, price)
# print(key, value)

user_input = input('***********************************\n** What would you\
 like to order? ''**\n***********************************\n')


# continue_order = input('***********************************\n** Are you finished with\
# your order? Type "quit" if yes''**\n***********************************\n')

counter = 1

if __name__ == "__main__":
    print('**************************************\n** Welcome to the Snakes\
    Cafe! **\n** Please see our menu below. **\n** To quit at any time,\
    type "quit" **\n**************************************')

while True:
    continue_order = input('***********************************\n** Are you finished\
with your order? Type "quit" if yes''**\n***********************************\n')
    if continue_order in menu.items():
        user_order.append(continue_order)
        print('Your current order consists of ' + str(user_order))
        counter += user_input
    """else:
        continue_order = 'quit()'
        print('***********************************\n** Your order has been completed\
        ''**\n***********************************\n')
        break
"""
