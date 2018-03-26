import snakes_cafe as cafe

def test_print_menu():
    pass

def test_user_input():
    pass

def test_valid_input():
    cafe.basket = {}
    assert cafe.add_order('rocks', 1) is None

def test_add_order():
    cafe.basket = {}
    cafe.add_order('Pie', 1)
    assert 'Pie' in cafe.basket

def test_valid_removie_item():
    cafe.basket = {}
    cafe.remove_item('plates')
    assert 'plates' in cafe.basket

def test_remove_item():
    cafe.basket = {'Pie': 1}
    cafe.remove_item('Pie')
    assert 'Pie' not in cafe.basket

# def test_item_category():
#     assert snakes_cafe.item_category('Sides') == """Sides

# Bread                         $2.00
# Hot Peppers                   $1.00
# Potatoes                      $3.00
# Bacon                         $5.00
# Apples                        $1.00
# Rice                          $4.00
# Noodles                       $4.00
# Eggs                          $3.00
# Corn                          $4.00
# Waffles                       $6.00
# Onions                        $2.00
# Chickpeas                     $4.00"""
