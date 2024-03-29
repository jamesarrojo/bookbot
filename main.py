def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(num_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    text_lower = text.lower()
    num_letters = {}
    for letter in text_lower:
        if letter.isalpha():
            if letter in num_letters:
                num_letters[letter] += 1
            else:
                num_letters[letter] = 1
    return num_letters

main()