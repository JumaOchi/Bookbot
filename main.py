def main() :
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f :
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    count = number_of_words(file_contents)
    print(f'{count} words found in the document\n')
    chara = sort_character_count(file_contents)
    for i in chara :
        for key, value in i.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

    


def number_of_words(file) :
    return len(file.split())


def character_count(file):
    # Convert the string to lowercase
    words = file.lower()

    characters = {}
    for letter in words:
        # Increment the count for the character in the dictionary
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_character_count(file) :
    character_dict = character_count(file)

    character_list = [{char:count} for char, count in character_dict.items() if char.isalpha()]
    character_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    return character_list



main()

