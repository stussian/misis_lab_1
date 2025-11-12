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