from stats import word_counter
from stats import letter_counter


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    words = word_counter(book_text)
    print(f"{len(words)} words found in the document")
    number_of_letters = letter_counter(words)
    print(number_of_letters)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    main()
