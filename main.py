def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    num_letters = filter_letters(num_chars)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for letter in num_letters:
        print(f"The '{list(letter.keys())[0]}' character was found {list(letter.values())[0]} times")
        
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    text_lower = text.lower()
    num_chars = {}
    for char in text_lower:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def filter_letters(chars):
    num_letters = []
    for char in chars:
        if char.isalpha():
            num_letters.append({char: chars[char]})
    def sort_on(dict):
        return list(dict.values())[0]

    num_letters.sort(reverse=True, key=sort_on)

    return num_letters

main()