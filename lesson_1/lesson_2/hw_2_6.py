a = int(input("Если хотите ввести данные о товаре введите 1: "))
k = 1
products =[]
analytics = {}
b = []

while a == 1:
    name = input('Введите название товара: ')
    price = input("Введите цену товара: ")
    quantity = input("Введите колличество товара: ")
    units = input("Введите единицу измерения: ")

    products_dict = {"название": name, "цена": price, "колличество": quantity, "ед": units}
    products_tuple = tuple([k, products_dict])
    products.append(products_tuple)
    k+=1
    a = int(input("Если хотите ввести данные о товаре введите 1: "))

# products = [(1, {'название': 'comp', 'цена': '1000', 'колличество': '10', 'ед': 't'}), (2, {'название': 'print', 'цена': '300', 'колличество': '3', 'ед': 't'})]


for i in products:
    a = i[1]
    for key, value in a.items():
        if key in analytics:
            c = analytics.get(key)
            c.append(value)
        else:
            b = [value]
            d = {key: b}
            analytics.update(d)
print(analytics)

