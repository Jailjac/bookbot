def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_word_count(text)
    character_frequency = get_character_count(text)
    sorted_character_frequency = character_dict_to_sorted_list(character_frequency)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document\n")

    for c in sorted_character_frequency:
        if not c['char'].isalpha():
            continue
        print(f"The '{c["char"]}' character was found {c["num"]} times")

    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_frequency = {}

    for c in text.lower():
        char_frequency[c] = char_frequency.get(c, 0) + 1

    return char_frequency

def sort_on(dict):
    return dict["num"]

def character_dict_to_sorted_list(characters):
    sorted_list = []
    for key, val in characters.items():
        expanded = {"char" : key, "num" : val}
        sorted_list.append(expanded)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)
        

main()