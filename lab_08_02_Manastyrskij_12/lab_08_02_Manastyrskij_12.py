with open('3.txt', 'r') as f:
    s = f.readline()
print(sum([s[i] == s[len(s) - 1 - i] for i in range(len(s) // 2)]))
