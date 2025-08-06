from stats import *
from sys import argv


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("============ BOOKBOT ============")
    text = get_book_text(argv[1])
    print(f"Analyzing book found at {argv[1]}")
    words_len = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {words_len} total words")
    print("--------- Character Count -------")
    letter_count = sort_letter_count(get_letter_count(text))
    for d in letter_count:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")


if __name__ == "__main__":
    main()
