my_rating = [7, 5, 3, 3, 2]
a = int(input('Введите новый элемент рейтинга: '))
if a > my_rating[0]:
    my_rating.insert(0, a)
else:
    my_rating.reverse()
    for i in my_rating:
        if a <= i:
            my_rating.insert(my_rating.index(i), a)
            break
    my_rating.reverse()
print(my_rating)

