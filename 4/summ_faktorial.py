N = int(input())
res = 1
summ = 0
for i in range(1, N + 1):
    res *= i
    summ += res
print(summ)
