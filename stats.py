def word_counter(book_text):
    words = book_text.split()
    return words


def letter_counter(words):
    char_counts = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter in char_counts:
                    char_counts[letter] += 1
                else:
                    char_counts[letter] = 1
    return char_counts


def chars_to_sorted_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})
    return char_list


def sort_on(char_list):
    return char_list["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def formatter(char_list):
    for char_dict in char_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
