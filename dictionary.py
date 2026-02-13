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
]


for index, seed in enumerate(sam_shop):
    print(index, ":", seed["name"])
buy = input("Which seed do you want to buy?")
while buy != ('no'):
    if buy == ('mango seed'):
        input("ok, the seed has been added to your cart. do you want to buy more?")
    elif buy == ('emberlily'):
        input("ok, the seed has been added to your cart. do you want to buy more?")
    elif buy == ('coconut seed'):
        input("ok, the seed has been added to your cart. do you want to buy more")
else:
    print("ok your total is:")

