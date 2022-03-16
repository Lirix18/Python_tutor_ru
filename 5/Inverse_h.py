string = 'In the hole in the ground there lived a hobbit'
pos1 = string.find('h')
pos2 = string.rfind('h')
s1 = string[:pos1 +1]
s2 = string[pos1+1:pos2:]
s3 = string[pos2:]
s = s1 + s2[::-1] + s3
print(s)
