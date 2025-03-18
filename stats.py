def get_num_words(words):
    return len(words)

def get_letters(s):
    letters = {}
    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def print_report(path, words, letters):
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {path} ...\n")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(words)} total words") 
    print("--------- Character Count -------")
    for x, y  in letters.items():
        print(f"{x}: {y}\n")