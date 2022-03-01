# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (пробелы важны!).
# The next number for the number 1534 is 1535.
# The previous number for the number 1534 is 1533.

num = int(input())
next = num + 1
previous = num - 1
print('The next number for the number '+ str(num) + ' is ' + str(next) + '.')
print('The previous number for the number ' + str(num) + ' is ' + str(previous) + '.')
