def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(book: str) -> int:
    word_list = book.split()
    return len(word_list)

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = word_count(book_contents)
    print(f"Found {num_words} total words")

main()
