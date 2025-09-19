fio = input()
con = [i for i in fio if i != ' ']
ini = [_ for _ in con if _.isupper()]
print(f'Инициалы: {''.join(ini)}')
print(f'Длина (символов): {len(con) + 2}')