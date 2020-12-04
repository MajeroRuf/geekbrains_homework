result = input('Введите строку: ')
my_list = result.split(' ')
k=1
for i in my_list:
    if len(i) > 10:
        print(f"{k}. {i[0:10]}")
        k+=1
    else:
        print(f"{k}. {i}")
        k+=1


