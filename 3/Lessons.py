l = int(input())
a = l * 45 + (l // 2)*5 + ((l + 1) // 2 - 1) * 15
# if lesson % 2 ==0:
#     h = 9 + ((s * lesson) + (p * (lesson // 2)) + (p2 * (lesson // 2 - 1))) // 60
#     m = ((s * lesson) + (p * (lesson // 2)) + (p2 * (lesson // 2 - 1))) % 60
# else:
#     h = 9 + ((s * lesson) + (p * (lesson // 2)) + (p2 * (lesson // 2))) // 60
#     m = ((s * lesson) + (p * (lesson // 2)) + (p2 * (lesson // 2))) % 60

print(a // 60 + 9, a % 60)