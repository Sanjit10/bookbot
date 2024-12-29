from curses.ascii import isalpha


def word_count():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words)

def char_count():
    letter_count_dict = {}
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if isalpha(letter):
                letter_count_dict[letter] = letter_count_dict.get(letter, 0) + 1
    return dict(sorted(letter_count_dict.items()))

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(), " words found in the document")
    for key, value in char_count().items():
        print(f"The '{key}' character was found {value} times")
    print('--- End report ---')

main()
