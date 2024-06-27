#!/usr/bin/env python3

import sys


def fetch_words(filepath):
    with open(filepath , 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    for item in items:
        print(item)

def main(filepath):
    words = fetch_words(filepath)
    print_items(words)


# fetch_words('text.txt')
if __name__ == '__main__':
    main(sys.argv[1])