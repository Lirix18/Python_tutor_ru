a = int(input())
b = int(input())
c = int(input())
if a > b and c > b:
    print(b)
elif b > c and a > c:
    print(c)
else: print(a)
