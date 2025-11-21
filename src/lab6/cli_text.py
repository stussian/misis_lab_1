import argparse
import sys
from pathlib import Path
from collections import Counter
from typing import Iterable
from src.lib.text import normalize, tokenize, count_freq, top_n


def read_lines(path: Path) -> Iterable[str]:
    """Простое чтение строк файла в UTF-8 с корректной обработкой ошибок."""
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            yield line


def run_cat(input_path: str, number_lines: bool) -> None:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    for idx, line in enumerate(read_lines(path), start=1):
        if number_lines:
            sys.stdout.write(f"{idx:6}\t{line}")
        else:
            sys.stdout.write(line)


def run_stats(input_path: str, top_n_value: int) -> None:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    text = path.read_text(encoding="utf-8", errors="replace")

    normalized = normalize(text)
    tokens = tokenize(normalized)
    freqs = count_freq(tokens)
    top = top_n(freqs, top_n_value)

    for word, count in top:
        print(f"{word}\t{count}")


# ===== НАСТРОЙКА ARGPARSE =====


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CLI-утилиты лабораторной №6 (работа с текстом)"
    )
    subparsers = parser.add_subparsers(
        dest="command", metavar="<command>", required=True
    )

    # --- подкоманда cat ---
    cat_parser = subparsers.add_parser(
        "cat", help="Вывести содержимое файла построчно"
    )
    cat_parser.add_argument(
        "--input",
        required=True,
        help="Путь к входному файлу",
    )
    cat_parser.add_argument(
        "-n",
        action="store_true",
        help="Нумеровать строки в выводе",
    )

    # --- подкоманда stats ---
    stats_parser = subparsers.add_parser(
        "stats", help="Показать частоты слов в тексте"
    )
    stats_parser.add_argument(
        "--input",
        required=True,
        help="Путь к входному текстовому файлу",
    )
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Сколько наиболее частотных слов показать (по умолчанию 5)",
    )

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "cat":
            run_cat(args.input, args.n)
        elif args.command == "stats":
            run_stats(args.input, args.top)
        else:
            parser.error(f"Неизвестная команда: {args.command}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()