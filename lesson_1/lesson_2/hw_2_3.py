#Вариант 1
my_dict = {1:'Зима', 2:'Зима', 12:'Зима',
           3:'Весна', 4:'Весна', 5:'Весна',
           6:'Лето', 7:'Лето', 8:'Лето',
           9:'Осень', 10:'Осень', 11:'Осень'}
month = int(input("Введите месяц: "))
print(my_dict.get(month))

#Вариант 2: Первый вариант не понравился из-за повторяющихся значений,
# казалось логичней, когда ключем выступает сезон, но тут возникли проблемы с выводом
#ключа по значению, не хватило опыта сообразить, как это делается, пришлось искать помощи в инете. :)

my_dict2 = {'Зима':(1, 2, 12),
            'Весна':(3, 4, 5),
            'Лето':(6, 7, 8),
            'Осень':(9, 10, 11)}
month_2 = int(input("Введите месяц: "))
for i in my_dict2.keys():
    if month_2 in my_dict2[i]:
        print(i)

#Вариант3
my_list = [None, 'Зима', 'Зима',
           'Весна', 'Весна', 'Весна',
           'Лето', 'Лето', 'Лето',
           'Осень', 'Осень', 'Осень',
           'Зима']
month_3 = int(input("Введите месяц: "))
print(my_list[month_3])