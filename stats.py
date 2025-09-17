def get_num_words(book: str) -> int:
    return len(book.split())

def get_char_count(book: str) -> int:
    s_book = book.lower()
    result = dict()
    for c in s_book:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

