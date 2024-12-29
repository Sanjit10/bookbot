from curses.ascii import isalpha
from collections import Counter
import string


def count_words_and_letters(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_contents = f.read().lower()

    words = file_contents.split()
    word_count = len(words)

    cleaned_words = [word.strip(string.punctuation) for word in words]
    letter_counts = Counter(letter for word in cleaned_words for letter in word if isalpha(letter))

    return word_count, dict(sorted(letter_counts.items()))


def main():
    filename = "./books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")

    word_count, letter_counts = count_words_and_letters(filename)
    print(f"{word_count} words found in the document")

    for letter, count in letter_counts.items():
        print(f"The '{letter}' character was found {count} times")

    print('--- End report ---')


if __name__ == "__main__":
    main()
