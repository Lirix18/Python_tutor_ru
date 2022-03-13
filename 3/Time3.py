a = float(31.05)

h = int(a // 30)
m = int((a % 30) / 0.5)
s = int((a % 0.5) * 120)

print(h, m, s)