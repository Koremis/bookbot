import sys
from stats import (
    word_counter,
    letter_counter,
    chars_to_sorted_list,
    formatter
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(["1"])
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    words = word_counter(book_text)
    char_counts = letter_counter(words)
    char_list = chars_to_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    print(formatter(char_list))
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    main()
