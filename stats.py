def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count
# This function takes a string as input, splits it into words, and returns the number of words.

letters = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0,
           "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
           "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "æ":0, "ë":0, "ï":0, "ö":0,
           "ü":0, "ß":0, "ñ":0, "ç":0, "á":0, "é":0, "í":0, "ó":0, "ú":0, "à":0,
           "è":0, "ì":0, "ò":0, "ù":0, "â":0, "ê":0, "î":0, "ô":0, "û":0, "å":0,
           "α":0, "β":0, "γ":0, "δ":0, "ε":0, "ζ":0, "η":0, "θ":0, "ι":0, "κ":0,
           "λ":0, "μ":0, "ν":0, "ξ":0, "ο":0, "π":0, "ρ":0, "σ":0, "τ":0, "υ":0,
           "φ":0, "χ":0, "ψ":0, "ω":0, "ά":0, "έ":0, "ή":0, "ί":0, "ό":0, "ύ":0,
           "ώ":0, "ς":0, "א":0, "ב":0, "ג":0, "ד":0, "ה":0, "ו":0, "ז":0, "ח":0,
           "ט":0, "י":0, "כ":0, "ל":0, "מ":0, "נ":0, "ס":0, "ע":0, "פ":0, "צ":0,
           "ק":0, "ר":0, "ש":0, "ת":0, "אּ":0, "בּ":0, "גּ":0, "דּ":0, "הּ":0, "וּ":0,
           "זּ":0, "חּ":0, "טּ":0, "יּ":0, "כּ":0, "לּ":0, "מּ":0, "נּ":0, "סּ":0, "עּ":0,
           "פּ":0, "צּ":0, "קּ":0, "רּ":0, "שּ":0, "תּ":0, "ϰ":0, "œ":0,}
# This dictionary contains all the letters in the English alphabet, as well as some special characters and letters from other languages, initialized to 0.

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