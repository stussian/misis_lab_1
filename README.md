# Лабораторные работы по дисциплине «Программирование и алгоритмизация» НИТУ МИСИС

Данный репозиторий создан для сдачи лабораторных работ по предмету **Программирование и алгоритмизация**  
обучающегося **Борискина Андрея Алексеевича**.

---

## 📂 Структура репозитория

```plaintext
python_labs/
├─ README.md
├─ src/
│  ├─ lib/
│  ├─ lab01/
│  ├─ lab02/
│  │  ├─ ex01.py
│  │  ├─ ex02.py
│  │  ├─ ex05.py
│  ├─ lab03/
│  ...
│  └─ lab10/
└─ images/
   ├─ lab01/
   ├─ lab02/
   │  ├─ img01.png
   │  ├─ img02.png
   │  ├─ img05.png
   ├─ lab03/
   ├─ lab04/
   ...
   └─ lab10/
```

# python_labs

## Лабораторная работа 1

### Задание 1

```python
  print(f'Привет {input()}! Через год тебе будет {int(input()) + 1}')
```

![ex1!](/image/lab1/img1.png)

### Задание 2

```python
a, b = float(input()), float(input())
print(f'sum: {a + b}; avg: {(a + b) / 2}')
```

![ex2!](/image/lab1/img2.png)

### Задание 3

```python
price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f'База после скидки: {base}')
print(f'НДС: {vat_amount}')
print(f'Итого к оплате: {total}')
```

![ex3!](/image/lab1/img3.png)

### Задание 4

```python
min = int(input())
print(f'{min//60}:{min % 60}')
```

![ex4!](/image/lab1/img4.png)

### Задание 5

```python
fio = input()
con = [i for i in fio if i != ' ']
ini = [_ for _ in con if _.isupper()]
print(f'Инициалы: {''.join(ini)}')
print(f'Длина (символов): {len(con) + 2}')
```

![ex5!](/image/lab1/img5.png)

### Задание 6

```python
k = int(input())
och = 0
zaoch = 0
for i in range(0, k):
    n = list(map(str, input().split()))
    if 'True' in n:
        och += 1
    else:
        zaoch += 1
print(och, zaoch)
```
![ex5!](/image/lab1/img6.png)

### Задание 7

```python
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
```

![ex5!](/image/lab1/img7.png)

## Лабораторная работа 2

### Задание 1 — arrays.py

```python
ddef min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    try:
        return ([min(nums), max(nums)])
    except ValueError:
        return 'ValueError'
    
print('----------min_max----------')
print(min_max([1, 2, 3, 4, 5]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
    
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    n = sorted(list(set(nums)))
    return n

print('----------unique_sorted----------')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    itog = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple): 
            for j in mat[i]:
                itog.append(j)
        else:
            return 'TypeError'
    return itog



print('----------flatten----------')
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![arrays!](/image/lab2/img1.png)

### Задание B — matrix.py

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'
    
    return [[mat[r][c] for r in range(len(mat))] for c in range(row_len)]
print('----------transpose----------')
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'
        
    return [sum(i) for i in mat]

print('----------row_sum----------')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            return 'ValueError'
    
    mat = transpose(mat)
        
    return [sum(i) for i in mat]

print('----------col_sums----------')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![matrix!](/image/lab2/img2.png)

### Задание C — tuples.py

```python
def info(fio: str, group: str, gpa: float) -> tuple:
    if not isinstance(fio, str):
        raise TypeError("fio должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("group должно быть строкой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("gpa должно быть числом")
    
    return ((lambda p: f"{p[0].capitalize()} {p[1][0].upper()}.{''+p[2][0].upper()+'.' if len(p)>2 else ''}")( [x.capitalize() for x in fio.strip().split() if x] ), group, f"{gpa:.2f}")

def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    inf = info(fio, group, gpa)
    answer = ''
    for _ in inf:
        answer += str(_)+ ', '
    return answer[:-2]

print('----------format_record----------')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![tuples!](/image/lab2/img3.png)

## Лабораторная работа 3

### Задание A — `src/lib/text.py`

```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.strip()

def tokenize(text: str) -> list[str]:
    text = re.findall(r'\b[\w\'-]+\b', text)
    return text

def count_freq(tokens: list[str]) -> dict[str, int]:
    dic = {}
    unique = set(tokens)
    for _ in unique:
        dic[_] = tokens.count(_)
    return dict(sorted(dic.items(), key=lambda x: (-x[1], x[0])))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
```

## Задание B — `src/text_stats.py` (скрипт со stdin)

```python
import sys
from lib.text import normalize, tokenize, count_freq, top_n

line = "ар ар ар а а а аб аб аб б б в в в в в в в в в" # sys.stdin.readline()

text = tokenize(normalize(line))
print(top_n(count_freq(text)))

max_len = len(sorted(text)[-1])

def info(Beautiful=False):
    if Beautiful:
        print(f'слово{' ' * (max_len - 5)} | частота')
        print(f'{'-' * (max_len + 10)}')

        for _ in top_n(count_freq(text)):
            print(f'{_[0]}{' ' * (max_len - len(_[0]))} | {_[1]}')
        return
    else:
        print(f'Всего слов: {len(text)}')
        print(f'Уникальных слов: {len(set(text))}')
        print(f'Топ-5:')
        for _ in top_n(count_freq(text)):
            print(f'{_[0]}:{_[1]}')

info(Beautiful=True)
```
![text_stats!](/image/lab3/img1.png)

## Лабораторная работа 4

### Задание A — модуль `src/lab04/io_txt_csv.py`

``` python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    try:
        return open(Path(path), encoding=encoding).readlines()
    except (FileNotFoundError or UnicodeDecodeError) as E:
        raise E
    
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if not rows:
        raise ValueError

    row_len = len(rows[0])
    for i, row in enumerate(rows):
        if len(row) != row_len:
            raise ValueError

    if header is not None and len(header) != row_len:
        raise ValueError

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        if header:
            writer.writerow(header)
        writer.writerows(rows)

txt = read_text("data/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
```

#### input.txt
![input!](/image/lab4/img1.png)

### Задание B — скрипт `src/lab04/text_report.py`

``` python
from pathlib import Path
from lab4.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n


def main():
    BASE_DIR = Path(__file__).resolve().parents[2]

    in_path = BASE_DIR / "data" / "lab4" / "input.txt"
    out_path = BASE_DIR / "data" / "lab4" / "report.csv"

    text = read_text(in_path)

    if isinstance(text, list):
        text = " ".join(text)

    text = normalize(text)
    tokens = tokenize(text)

    freq = count_freq(tokens)

    write_csv(list(freq.items()), out_path, header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:", top_n(freq))


if __name__ == "__main__":
    main()
```

#### check_2.csv
![check2!](/image/lab4/imgs2.png)