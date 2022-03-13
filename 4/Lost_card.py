N = int(input())
summ = 0
for i in range(1, N + 1):
    summ += i
for i in range(N - 1):
    num = int(input())
    summ -= num
print(summ)