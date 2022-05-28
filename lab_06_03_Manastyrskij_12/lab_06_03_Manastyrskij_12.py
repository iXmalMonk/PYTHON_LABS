str = input('STR: ')
symbol = input('SYMBOL: ')

while True:
    if symbol in str:
        print(str[0:str.find(symbol)])
        str = str[str.find(symbol) + 1:len(str)]
    else:
        break

# 12. Вывести на экран слова строки, после которых стоит указанный
# пользователем знак препинания.
