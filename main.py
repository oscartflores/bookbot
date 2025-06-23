def get_book_text(path):
    files_contents=""
    with open(f"books/{path}") as f:
        files_contents = f.read()
    return files_contents


def word_count(): 
    count = 0
            # Start to split text into single words
    for words in get_book_text:
        w_split = words.split()     
            # Next loop to count words 
        for w in w_split:
            count += 1
    return count

def main():
    get_book_text = "frankenstein.txt"
    book = word_count
    print(f"{book} words found in the document")
  # text = get_book_text("frankenstein.txt")
#print(text)


main()