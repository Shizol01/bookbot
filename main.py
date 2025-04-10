from stats import word_count, character_count
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as path:
        book = path.read()
    return book




def main():
    try:
        title = sys.argv[1]
    except IndexError as e:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    
    

    book = get_book_text(title)
    num_words = word_count(book)
    char_count = character_count(book)

    print(f"""============ BOOKBOT ============
Analyzing book found at {title}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for char in char_count:
        print(char)
    print("============= END ===============")

main()