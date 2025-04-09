import string

def char_counter(text):
    letter_dict = {}
    
    for char in text:
        char = char.lower()
        if char in letter_dict:
            letter_dict[char] +=1
        else:
            letter_dict[char] = 1

    return letter_dict


def sort_chars(char_dict):

    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list



def words_number(text):
        words = text.split()
        number = len(words)
        return number