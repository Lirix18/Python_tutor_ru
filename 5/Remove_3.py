string = input()
res = ''
for i in range(len(string)):
    if i % 3 != 0:
        res += string[i]
print(res)

