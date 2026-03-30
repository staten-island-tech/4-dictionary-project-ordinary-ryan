sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def recipt(Food):
    the_recipt = {}
    for sushi in Food:
        if sushi['name'] in the_recipt:
            continue
        else:
            the_recipt[sushi['name']] = {
                'price': sushi['price'],
                'qty'  : 1
            }
        print(the_recipt)
recipt(sushi_orders)
      