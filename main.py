from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        path = sys.argv[1]
        with open(path) as book: 
            text = book.read()
            words = text.split()
            alpha_only = ''.join(filter(str.isalpha, text)).lower()
            letters = get_letters(alpha_only)
            print_report(path,words,letters)
main()
