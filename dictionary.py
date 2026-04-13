sam_shop = [
{
    "name": "mango seed",
    "price" : 100000,
    "rarity" : "mythical",
    "description": "A mythical fruit that has a 1.25 to 1.5 percent chance of stocking in the shop. Spawns a fruit every 2 minutes after maturity."
},
{
    "name": "ember lily seed",
    "price" : 15000000,
    "rarity" : "prismatic",
    "description": "A prismatic flower that has around a 0.03 percent chance of stocking in the shop. Spawns a flower every 6 hours after maturity."
},
{
    "name": "coconut seed",
    "price" : 6000,
    "rarity" : "mythical",
    "description": "A mythical seed that has around a 0.35 percent chance of stocking in the shop. Spawns up to 20 coconuts every 20 minutes after maturity after maturity."
},
{
    "name": "strawberry seed",
    "price": 1200,
    "rarity": "common",
    "description": "A sweet berry plant that has a high chance of stocking in the shop. Spawns strawberries every 2 minutes after maturity."
},
{
    "name": "pumpkin seed",
    "price": 4500,
    "rarity": "uncommon",
    "description": "A chunky autumn crop that has a moderate chance of stocking in the shop. Spawns pumpkins every 6 minutes after maturity."
},
{
    "name": "cactus seed",
    "price": 18000,
    "rarity": "rare",
    "description": "A desert plant with a low chance of stocking in the shop. Spawns cactus fruit every 12 minutes after maturity."
},
{
    "name": "glow mushroom seed",
    "price": 95000,
    "rarity": "mythical",
    "description": "A magical glowing mushroom that has a very low chance of stocking in the shop. Spawns glow mushrooms every 25 minutes after maturity."
}
]


for index, seed in enumerate(sam_shop):
    print(index, ":", seed["name"])
cart = []
total = 0
start = True


while start:
    buy = input("Which seed do you want to buy?")
    for seed in sam_shop:
        if seed["name"] == buy:
            cart.append(seed["name"])
            total += seed["price"] 
            print(cart)
            print("ok, the seed has been added to your cart.")
            break
            

    cont = input("do you want to buy more? yes or no:")
    if cont == 'no':
        start = False


else:         
    print(cart)
    print("Your total is:", total)


