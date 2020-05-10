d = {}
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 150},
    {'title': 'Nokia', 'price': 110}
]

print(products)

for product in products:
    print(product['title'], product['price'])

product1 = dict(
    title='iPhone',
    price=110
)

print(product1['title'])
for key in product1:
    print(product1[key])

users = [
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'John']
]

d_users = dict(users)

print(d_users)