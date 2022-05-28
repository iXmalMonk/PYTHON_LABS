str = input('STR: ')
i = 0
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ'
while i < len(str):
    if str[i] in str:
        alphabet = alphabet.replace(str[i], '', 1)
    i += 1

print(alphabet)
# 12. Дан текст. Каких прописных русских букв в нем нет?
