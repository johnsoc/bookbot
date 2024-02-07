def main():
    book = read_book()
    words = count_words(book)
    characters = character_count(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"The word count is {words}")
    print_report(characters)
    print("--- End report ---")


def read_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    return len(text.split())

def character_count(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def print_report(dict):
    characters = []
    for a in dict:
        if a.isalpha():
            characters.append({"name": a, "num": dict[a]})
    characters.sort(reverse=True, key=sort_on)
    for char in characters:
        print(f"The character {char["name"]} appeared {char["num"]} times ")
    
main()