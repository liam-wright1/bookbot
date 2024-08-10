def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #print(word_count(text))
    #print(char_count(text))
    print(f"--- Begin report of {book_path} ---")
    print(word_count(text))
    print("")
    report(text)
    print("--- End report ---")

    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    lst = text.split()
    lst_len = f"Word Count = {len(lst)}"
    return lst_len

def char_count(text):
    char_num = {}
    lower = text.lower()
    for char in lower:
        if char.isalpha() and char in char_num:
            char_num[char] += 1
        elif char.isalpha():
            char_num[char] = 1
    return char_num

def sort_on(dict):
    return dict["num"]

def report(text):
    char_num = {}
    lower = text.lower()
    for char in lower:
        if char.isalpha() and char in char_num:
            char_num[char] += 1
        elif char.isalpha():
            char_num[char] = 1

    char_list = []
    for key, value in char_num.items():
        new_dict = {"char": key, "num": value}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
main()