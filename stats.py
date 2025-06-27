def word_count(path):
    with open(path) as f:
        files_contents = f.read()
    split_contents = files_contents.split()
    count = len(split_contents)
    return count

       
       
        # Where characters will go into
character_dict = {}
        # Function to count the amount of letters are seen in a book
def char_count(path):
    #character_dict = {}
    with open(path) as f:
        files_contents = f.read()
        lower_case = files_contents.lower()
        for letters in lower_case:
            if letters.isalpha():
                if letters not in character_dict:
                    character_dict[letters] = 1
                else:
                    character_dict[letters] += 1
    return character_dict

def sort_on(items):
    return items["num"]
    
def sort_characters(character_dict):
    characters = []
    for char, num in character_dict.items():
        characters.append({"char": char, "num": num})
    
    characters.sort(reverse=True, key=sort_on)
    return characters

  