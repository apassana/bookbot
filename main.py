import stats
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = stats.get_num_words(book)
    char_count = stats.get_char_count(book)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for i in sorted(char_count):
        if i.isalpha():
            print(f'{i}: {char_count[i]}')
    print('============= END ===============')


if __name__ == "__main__":
    main()
