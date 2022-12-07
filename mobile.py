mobile_data = {
    'status': True, 'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

i = 0
while i < len((mobile_data["data"])):
    name = (mobile_data["data"][i].get('name'))
    price = (mobile_data["data"][i].get('price'))
    made = (mobile_data["data"][i].get('made'))
    i += 1

    split_price = price.split()
    usd_to_bdt = float(split_price[0])*100

    sentence = f"The {name} released in last year. This phone is manufractured by {made}. Good " \
               f"news is the {name} is now available in Bangladesh with price {usd_to_bdt} bdt."

    print(sentence)
