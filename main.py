
def main():
    book_path = 'books/frankenstein.txt'
    print(f'--- Begin report of {book_path} ---')
    file_contents = get_book_text(book_path)
    number_of_words = len(file_contents.split())
    print(f'{number_of_words} words found in the document\n')

    occurences_dict = get_char_dict(file_contents)
    occurences_list = [{'char': x, 'num': occurences_dict[x]}
                       for x in occurences_dict if x.isalpha()]

    occurences_list.sort(reverse=True, key=sort_on)

    for char in occurences_list:
        print(f'The \'{char['char']}\' was found {char['num']} times')

    print('--- End report ---')


def sort_on(dict):
    return dict['num']


def get_char_dict(text):
    occurences = {}

    for word in text.split():
        for char in word:
            char = char.lower()
            occurences[char] = occurences.get(char, 0) + 1

    return occurences


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
