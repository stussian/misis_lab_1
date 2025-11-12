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