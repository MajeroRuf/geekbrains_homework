sec = input("Веедите колличество секунд:")
sec = int(sec)
hh = sec // 3600
dd = hh // 24
mm = (sec - (hh * 3600)) // 60
ss = (sec - (hh * 3600)) % 60
if dd > 0:
    hh = sec // 3600 % 24
    stroka = f"Time: {dd} дн {hh:02}:{mm:02}:{ss:02}"
    print(stroka)
else:
    stroka = f"Time: {hh:02}:{mm:02}:{ss:02}"
    print(stroka)