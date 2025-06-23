def word_count(path):
    files_contents=""
    with open(f"books/{path}") as f:
        files_contents = f.read()
    split_contents = files_contents.split()
    count = len(split_contents)
    return count
