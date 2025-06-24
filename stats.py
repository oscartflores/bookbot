def word_count(path):
    with open(f"books/{path}") as f:
        files_contents = f.read()
    split_contents = files_contents.split()
    count = len(split_contents)
    return count

def char_count(path):
    character_dict = {}
    with open(f"books/{path}") as f:
        files_contents = f.read()
        lower_case = files_contents.lower()
        for letters in lower_case:
            if letters not in character_dict:
                character_dict[letters] = 1
            else:
                character_dict[letters] += 1
    return character_dict

    



def main():
    book = char_count("frankenstein.txt")
    print(book)

main()
    