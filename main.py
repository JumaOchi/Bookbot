def main() :
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f :
        file_contents = f.read()

    #print(file_contents)
    count = number_of_words(file_contents)
    chara = character_count(file_contents)
    print(chara)

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



main()

