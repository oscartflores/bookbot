from stats import word_count
from stats import char_count
from stats import sort_on
from stats import sort_characters
def main():
    filename = "frankenstein.txt"
    book = char_count(filename)
    w_count = word_count(filename)
    sorted_characters = sort_characters(book)
   
    print(
        f"""
    ============ BOOKBOT ============
    Analyzing book found at books/{filename}...
    ----------- Word Count ----------
    Found {w_count} total words   
    --------- Character Count -------       
        """
    )
    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
main()

