from stats import word_count, letter_count

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = word_count(book_contents)
    letter_dict = letter_count(book_contents)
    print(f"Found {num_words} total words")
    print(letter_dict)


main()
