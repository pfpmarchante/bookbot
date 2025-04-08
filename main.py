from stats import (
    get_num_words, get_char_frequency, sort_dict
    )
import sys

def get_book_text(path):
    """
    Reads the contents of a book file and returns the text.
    :param path: Path to the book file.
    :return: Text of the book.
    """
    with open(path) as f:
        text = f.read()
    return text

# Main code
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
    
book_text = get_book_text(path)
word_count = get_num_words(book_text)
char_count = get_char_frequency(book_text)
sorted_dict = sort_dict(char_count)


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_dict:
        char = entry.get('char')
        count = entry.get('count')
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
        
    print("============= END ===============")
    
main()

    


