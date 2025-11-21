import json
import csv
from pathlib import Path


def _check_path(path_str, suffix):
    path = Path(path_str)
    if path.is_absolute():
        raise ValueError("Путь должен быть относительным")
    if path.suffix.lower() != suffix:
        raise ValueError("Неверный тип файла")
    return path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = _check_path(json_path, ".json")
    csv_file = _check_path(csv_path, ".csv")

    if not json_file.exists():
        raise FileNotFoundError(json_path)

    text = json_file.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("Пустой JSON")

    try:
        data = json.loads(text)
    except Exception:
        raise ValueError("Некорректный JSON")

    if not isinstance(data, list) or not data:
        raise ValueError("Ожидается непустой список объектов")
    if not all(isinstance(x, dict) for x in data):
        raise ValueError("Элементы должны быть dict")

    keys = sorted({k for obj in data for k in obj})
    if not keys:
        raise ValueError("Нет полей")

    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = _check_path(csv_path, ".csv")
    json_file = _check_path(json_path, ".json")

    if not csv_file.exists():
        raise FileNotFoundError(csv_path)

    text = csv_file.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("Пустой CSV")

    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Нет заголовка")

        rows = []
        for row in reader:
            rows.append({k: ("" if v is None else str(v)) for k, v in row.items()})

    if not rows:
        raise ValueError("Нет данных")

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Задание 1
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    path = Path("data/out/people.json")

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with path.open("r", encoding="utf-8") as f:
        loaded = json.load(f)


    # Задание 2
    rows = [
        {"name": "Alice", "age": "22", "city": "SPB"},
        {"name": "Bob", "age": "25", "city": "Moscow"}
    ]

    with open("data/out/people.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    with open("data/out/people.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

        
