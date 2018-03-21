import snakes_cafe

def test_print_menu():
    assert snakes_cafe.print_menu() == '''Wings: 8.0
Spring Rolls: 5.0
Cookies: 2.0
Grilled Squid: 8.0
Crab Wonton: 6.0
Satay: 7.0
Salmon: 15.0
Steak: 20.0
Meat Tornado: 25.0
A Literal Garden: 12.0
Pad Thai: 10.0
Spicy Meatballs: 12.0
Ice Cream: 6.0
Cake: 6.0
Pie: 7.0
Mango with Sicky Rice: 6.0
Mushroom Yogurt: 5.0
Popsicle: 3.0
Coffee: 3.0
Tea: 2.0
Blood of the Innocent: 50.0
Champagne: 8.0
Martini: 11.0
Italian Lemondrop: 10.0
Bread: 2.0
Hot Peppers: 1.0
Potatoes: 3.0
Bacon: 5.0
Apples: 1.0
Rice: 4.0
'''

def test_user_input():
    assert snakes_cafe.user_input_to_list() == ['']
