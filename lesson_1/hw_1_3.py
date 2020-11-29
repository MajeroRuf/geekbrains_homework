n = input("Введите число: ")
n = int(n)
i = 1
p = n
s = n
while i < n:
    p = "%s%s" % (p, n)
    p = int(p)
    s = s + p
    i += 1
print(s)