from stats import word_count
from stats import char_count
def main():
    book = word_count("frankenstein.txt")
    print(f"{book} words found in the document")

main()
