P = 17
X = 94
Y = 41
before = X * 100 + Y
sum = before + (before / 100) * P
print(int(sum // 100), int(sum % 100))