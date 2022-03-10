import math

a = int(input())
b = int(input())
n = int(input())

print(math.ceil(a * n + (b * n) // 100))
print(math.ceil(b * n % 100))