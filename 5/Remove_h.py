string = 'In the hole in the ground there lived a hobbit'
pos1 = string.find('h')
pos2 = string.rfind('h')
h = string.split('h')
print(h[0] + h[-1])

# s = input()
# s = s[:s.find('h')] + s[s.rfind('h') + 1:]
# print(s)