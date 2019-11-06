get_order = lambda o :''.join([f'{m.title()} ' * o.count(m) for m in ['burger','fries','chicken','pizza','sandwich','onionrings','milkshake','coke']])[:-1]

'''
def get_order(order):
    meals = [
                'burger',
                'fries',
                'chicken',
                'pizza',
                'sandwich',
                'onionrings',
                'milkshake',
                'coke'
            ]
    taken = ''
    for meal in meals:
        taken += f'{meal.title()} ' * order.count(meal)
    return taken.strip()
'''
