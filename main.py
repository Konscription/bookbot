def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    count_by_letter = get_letter_count(book_text)
    print_report(book_path,word_count,count_by_letter)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]
#sort dict
def sort_dict(list):
    list.sort(reverse=True, key=sort_on)
    return list

#Count Letters
def get_letter_count(text):
    lowered_string = text.lower()
    unique_characters = ''.join(set(lowered_string))
    character_counts_sortable = []
    for char in unique_characters:
        if char.isalpha():
            character_counts= {}
            char_count = lowered_string.count(char)
            character_counts["char"] = char
            character_counts["count"] = char_count
            character_counts_sortable.append(character_counts)
    return sort_dict(character_counts_sortable)


def print_report(book_path,word_count_total,count_by_letter):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count_total} words found in the book.\n")
    for entry in count_by_letter:
        print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()
    