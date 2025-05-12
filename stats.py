def get_word_count(text):
    num_words = text.split()
    return len(num_words)


def get_char_count(text):
    char_dict = {}
    for letter in text:
        lower_letter = letter.lower()

        if lower_letter in char_dict:
            char_dict[lower_letter] += 1
        else:
            char_dict[lower_letter] = 1

    return char_dict


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
