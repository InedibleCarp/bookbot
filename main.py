import sys
from stats import word_counter, character_counts, character_sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    current_book = sys.argv[1]
    book_text = get_book_text(current_book)
    num_words = word_counter(book_text)
    character_dictionary = character_counts(book_text)
    character_list = character_sort(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in character_list:
        if entry["char"].isalpha() == False:
            continue
        print(f"{entry['char']}: {entry['num']}")
    
if __name__ == "__main__":
    main()