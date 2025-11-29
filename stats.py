def word_count(book: str) -> int:
    word_list = book.split()
    return len(word_list)

def letter_count(book: str) -> dict:
    letter_dict = {}

    lower_book = book.lower()

    for letter in lower_book:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def build_report(letter_dict: dict, book_path: str, num_words: int) -> None:
    letter_dict.sort()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

