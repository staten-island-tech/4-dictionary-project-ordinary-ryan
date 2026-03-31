""" sushi_orders = [
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
            the_recipt[sushi['name']]['qty'] +=1
        else:
            the_recipt[sushi['name']] = {
                'price': sushi['price'],
                'qty'  : 1
            }  
    for sushi, value in the_recipt.items():
        price = value['price']*value['qty']
        print(sushi,value['qty'], price)

recipt(sushi_orders)
       """

wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def ward(department):
    staff = {}
    for dep, ppl in wards.items():
        print(ppl, dep)
    
    
"""   for ppl in department:
            if ppl['name'] in dep:
                staff[ppl['name']]['job'] += ppl['name']
            print(staff) """