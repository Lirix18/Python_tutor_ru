import math
string = input()
a = math.ceil(len(string)/2)
res = string[a:] + string[:a]
print(res)