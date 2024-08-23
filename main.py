def main():
    path = ('books/frankenstein.txt')
    with open(path) as book: 
        text = book.read()
        words = text.split()
        alphaOnly = ''.join(filter(str.isalpha, text)).lower()
        letters = {}

        for letter in alphaOnly:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        
        print(f"--- Begin Report of {path} ---\n")
        print(f"Total Words: {len(words)}\n")
        print(f"Unique Letters: {len(letters)}\n")
        print(f"Most Frequent Letter: {max(letters, key=letters.get)}\n")
        for x, y  in letters.items():
            print(f"The character {x} was found {y} times.\n")

main()
