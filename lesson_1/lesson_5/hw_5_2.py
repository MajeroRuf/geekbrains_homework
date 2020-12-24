"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('data_wiki.txt', 'r') as d_obj:
    cnt_l = 0
    cnt_s = 0
    for line in d_obj:
        cnt_l += 1
        cnt_s = len(line)
        print(f' В строке {cnt_l}: {cnt_s} симв.')
    print(f' В файле {d_obj.name}: {cnt_l} строк.')