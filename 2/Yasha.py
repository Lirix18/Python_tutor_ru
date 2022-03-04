N = int(input())
M = int(input())
x = int(input())
y = int(input())
MaX = max(N, M)
MiN = min(N, M)
N = MaX - y
M = MiN - x
print(min(x,y,M,N))
