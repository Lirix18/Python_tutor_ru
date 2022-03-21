string = input()
# string = 'In the hole in the ground there lived a hobbit'
pos1 = string.find('h')
pos2 = string.rfind('h')
string2 = string[:pos1+1] + string[pos1+1:pos2].replace('h', 'H') + string[pos2:]
print(string2)