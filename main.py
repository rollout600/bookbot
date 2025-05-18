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
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # This function checks if the correct number of command line arguments are provided. If not, it prints usage instructions and exits.
    
    #variables to be set
    path_to_file = sys.argv[1] 
    file_contents = get_book_text(path_to_file)
    letter_count = char_count(file_contents)
    sorted = sort_dict(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(file_contents)} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted)):
        if sorted[i]['num'] == 0:
            continue
        else:
            print(f"{sorted[i]['letter']}: {sorted[i]['num']}")
# This function defines the main function that will be executed when the script is run.

main()