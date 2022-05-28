import csv

def c1():
    r, c = map(int, input("Введите r, c для матрицы: ").split())
    arr = [0] * r
    for i in range(r):
        arr[i] = [0] * c

    for i in range(r):
        for j in range(c):
            if i > j:
              arr[i][j] = i - 2 * j
            elif i < j:
              arr[i][j] = 3 * i + j
            else:
               arr[i][j] = i * j

    for row in arr:
        for elem in row:
            print(elem, end = ' ')
        print()

    print(arr)

    with open('arr.csv', 'w', newline = '') as f:
        fW = csv.writer(f)
        fW.writerows(arr)

def c2():
    a = []
    with open('arr.csv', 'r') as f:
        fR = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
        for row in fR:
            a.append(row)
    print(a)

while(True):
    c = int(input("1. Создать и записать матрицу в файл\n2. Прочитать матрицу из файла\nC = "))
    if 1 <= c <= 2:
        break

if c == 1:
    c1()
else:
    c2()