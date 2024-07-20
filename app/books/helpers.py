def next_book_id(book_collection):
    return 1 if len(book_collection) == 0 else book_collection[-1].id + 1
    