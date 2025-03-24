from stats import word_counter


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    number_of_words = word_counter(book_text)
    print(f"{number_of_words} words found in the document")

    # print(book_text)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    main()
