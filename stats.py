def word_counter(book_text):
    return len(book_text.split())

def character_counts(book_text):
    lowercase_book = book_text.lower()
    character_book = {}
    
    for character in lowercase_book:
        if character in character_book:
            character_book[character] += 1
        else:
            character_book[character] = 1
    return character_book

def character_sort(character_book):
    def sort_on(items):
        return items["num"]
    
    characters_list = []
    
    for key,value in character_book.items():
        characters_list.append({"char": key, "num": value})
        
    characters_list.sort(reverse=True, key=sort_on)
    
    return characters_list