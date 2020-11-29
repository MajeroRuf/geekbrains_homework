n = int(input("Введите число: "))
s = n // 10
p = n % 10
p1 = 0
while s != 0:
    p1 = s % 10
    s = s // 10
    if p1 > p:
        p = p1
print(p)