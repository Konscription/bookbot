def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the book.")
    print(get_letter_count(book_text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

#Count Letters
def get_letter_count(text):
    lowered_string = text.lower()
    unique_characters = ''.join(set(lowered_string))
    character_counts = {}
    for char in unique_characters:
        char_count = lowered_string.count(char)
        character_counts[char] = char_count
    return character_counts

def log(text,is_debug):
    if is_debug:
        print(text)

main()
    