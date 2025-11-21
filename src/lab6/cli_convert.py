import argparse
import sys
from pathlib import Path
from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_to_xlsx


def ensure_input_exists(path_str: str) -> Path:
    path = Path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"Входной файл не найден: {path}")
    return path


def run_json2csv(inp: str, out: str) -> None:
    ensure_input_exists(inp)
    json_to_csv(inp, out)


def run_csv2json(inp: str, out: str) -> None:
    ensure_input_exists(inp)
    csv_to_json(inp, out)


def run_csv2xlsx(inp: str, out: str) -> None:
    ensure_input_exists(inp)
    csv_to_xlsx(inp, out)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CLI-конвертеры данных (ЛР6)"
    )
    sub = parser.add_subparsers(dest="cmd", metavar="<command>", required=True)

    # json2csv
    p1 = sub.add_parser(
        "json2csv", help="Конвертация JSON → CSV"
    )
    p1.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Входной JSON-файл",
    )
    p1.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному CSV-файлу",
    )

    # csv2json
    p2 = sub.add_parser(
        "csv2json", help="Конвертация CSV → JSON"
    )
    p2.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Входной CSV-файл",
    )
    p2.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному JSON-файлу",
    )

    # csv2xlsx
    p3 = sub.add_parser(
        "csv2xlsx", help="Конвертация CSV → XLSX"
    )
    p3.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Входной CSV-файл",
    )
    p3.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному XLSX-файлу",
    )

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.cmd == "json2csv":
            run_json2csv(args.input, args.output)
        elif args.cmd == "csv2json":
            run_csv2json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            run_csv2xlsx(args.input, args.output)
        else:
            parser.error(f"Неизвестная команда: {args.cmd}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except NotImplementedError as e:
        # Если забыли подключить функции из ЛР5
        print(f"Ошибка конфигурации: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()