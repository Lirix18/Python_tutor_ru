l = int(input())
a = l * 45 + (l // 2)*5 + ((l + 1) // 2 - 1) * 15

print(a // 60 + 9, a % 60)