number_of_letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
alphabet = "abcdefghijklmnopqrstuvwxyz"


def word_counter(book_text):
    words = book_text.split()
    return words


def letter_counter(words):
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in alphabet:
                number_of_letters[letter] += 1
    return number_of_letters
