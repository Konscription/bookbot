def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the book.")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

#Count Letters
def get_letter_count(text):
    lowered_string = text.lower()
    

main()
    