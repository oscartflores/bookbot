def word_count(path):
    with open(f"books/{path}") as f:
        files_contents = f.read()
    split_contents = files_contents.split()
    count = len(split_contents)
    return count

       
       
        # Where characters will go into
character_dict = {}
        # Function to count the amount of letters are seen in a book
def char_count(path):
    #character_dict = {}
    with open(f"books/{path}") as f:
        files_contents = f.read()
        lower_case = files_contents.lower()
        for letters in lower_case:
            if letters not in character_dict:
                character_dict[letters] = 1
            else:
                character_dict[letters] += 1
    return character_dict

def sort_on(items):
    return items["num"]
    
def sort_characters(character_dict):
    characters = []
    for char, num in character_dict():
        characters.append({"char": char, "num": num})
    
    characters.sort(reverse=True, key=sort_on)
    return characters

def main():
    book = char_count("frankenstein.txt")
    sorted_characters = sort_characters(book)
    print(sorted_characters)

main()
    


#def stats():
   # character_dict.sort()
   # return """============ BOOKBOT ============
   # Analyzing book found at books/frankenstein.txt...
  #  ----------- Word Count ----------
  #  Found 75767 total words
  #  --------- Character Count -------
#"""
  