import sys
from stats import words_number, char_counter, sort_chars





def get_book_text(filepath):
    try:
        with open(filepath) as f:
            text = f.read()
        return text  
    except FileNotFoundError:
        print(f"Error: Cannot find the file at {filepath}")
        sys.exit(1)
   



def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    liczba = words_number(text)
    dictionary = char_counter(text)  
    sort_dic = sort_chars(dictionary)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {liczba} total words")
    print("----------- Character Count ----------")
    for dictionary in sort_dic:
        char = dictionary["char"]
        count = dictionary["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    

main()


