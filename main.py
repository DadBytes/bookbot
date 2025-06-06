import sys

from stats import chars_dict_to_sorted_list, get_char_count, get_word_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)
    print_report(book_path, num_words, char_sorted_list)


main()
