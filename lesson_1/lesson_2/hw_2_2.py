result = input("Введите значения списка через пробел: ")
first_list = result.split(' ')
k = 0
for i in range(int(len(first_list)/2)):
    first_list[k], first_list[k+1] = first_list[k+1], first_list[k]
    k +=2
print(first_list)
