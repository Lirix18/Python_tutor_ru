string = 'hello'
if string.count('f') == 1:
    print(string.find('f'))
elif string.count('f') >= 2:
    print(string.find('f'), string.rfind('f'))
