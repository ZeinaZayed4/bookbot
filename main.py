import sys
from stats import num_of_words, char_count, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_contents = get_book_text(filepath)

    words_count = num_of_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")

    character_counts = char_count(book_contents)
    sorted_chars = sort_char_counts(character_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
