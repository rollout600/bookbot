file_contents = ""
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
# This function reads the contents of a file and returns it as a string.

from stats import word_count
# This function imports the word_count function from the stats module.

letter_count = {}
from stats import char_count
# This function imports the char_count function from the stats module.

sorted = []
from stats import sort_dict
# This function imports the sort_dict function from the stats module.

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    letter_count = char_count(file_contents)
    sorted = sort_dict(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(file_contents)} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted)):
        print(f"{sorted[i]['letter']}: {sorted[i]['num']}")
# This function defines the main function that will be executed when the script is run.

main()