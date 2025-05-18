def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count
# This function takes a string as input, splits it into words, and returns the number of words.

letters = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0,
           "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
           "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "æ":0, "ë":0, "ï":0, "ö":0,
           "ü":0, "ß":0, "ñ":0, "ç":0, "á":0, "é":0, "í":0, "ó":0, "ú":0, "à":0,
           "è":0, "ì":0, "ò":0, "ù":0, "â":0, "ê":0, "î":0, "ô":0, "û":0, "å":0,}
def char_count(file_contents):
    lowercase = file_contents.lower()
    for char in lowercase:
        if char.isalpha():
            letters[char] += 1
    return letters
# This function takes a string as input, converts it to lowercase, and counts the occurrences of each letter in the string.


def sort_dict(letters):
    def sort_on(sorted):
        return sorted["num"]
    sorted = []
    for letter in letters:
        sorted.append({"letter": letter, "num": letters[letter]})

    sorted.sort(reverse=True, key=sort_on)
    return sorted
# This function takes a dictionary of letters and their counts, sorts it in descending order, and returns the sorted list.