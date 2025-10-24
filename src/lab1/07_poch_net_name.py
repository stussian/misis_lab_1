N = input()
con = 1
name = ''
for i in range(0, len(N)):
    if N[i].isupper():
        name += N[i]
        for j in range(i, len(N)):
            if N[j].isnumeric():
                for _ in range(j + 1, len(N), con):
                    name += N[_]
                break
            con += 1
print(name)