def main():
    file_contents = get_text("books/frankenstein.txt")

    # words = word_count(file_contents)
    # print(words)

    dict_char = char_count(file_contents)
    # print(dict_char)

    char_report(dict_char)


def get_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    dict_char = {}

    for i in text:
        j = i.lower()
        if j not in dict_char:
            dict_char[j] = 1
        else:
            dict_char[j] += 1
    return dict_char

def char_report(dict_char):
    for i in dict_char:
        if i.isalpha():
            print(f"The '{i}' character was found {dict_char[i]} times")
        


main()
