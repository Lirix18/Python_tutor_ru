# массив с булевыми значениями, 2 значения для 3 переменных = 2^3 =8
# 8 строк по 3 значения = 24. Тут многомерный массив, в лист 8 вложенных массивов
list = [
    ['False False False'],
    ['False False True'],
    ['False True False'],
    ['False True True'],
    ['True False False'],
    ['True False True'],
    ['True True False'],
    ['True True True']
]


# функция вычесления закона Де Моргана
# == имеет выше приоритет чем not.
# у тебя было (x or y or z) == (not x)
def checkPredikatbool(x, y, z):
    if (not (x or y or z)) == ((not x) and (not y) and (not z)):
        print('True')
    else:
        print('False')

# берем элемент массива и делаем из него новый, по разделителю пробел
# и из этого массива берем 1,2,3-й элементы в твою функцию
for i in list:
    listbool = str(i).split()
    checkPredikatbool(listbool[0], listbool[1], listbool[2])



