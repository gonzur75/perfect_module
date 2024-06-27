#!/usr/bin/env python3

"""Fetch and print words

Usage:
    python main.py <filepath>
    ./main.py <filepath>
    shell:
    from main import main
    main(<failpath>)

"""

import sys


def fetch_words(filepath):
    """
    Fetch words from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: word list from given filepath
    :rtype: list[str]
    """
    with open(filepath , 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    """
     Print items from given iterable
     :param items: any iterable collection of data
     :type items: iterable
     :return: None
     :rtype: None
     """
    for item in items:
        print(item)

def main(filepath):

    """
    Feth and print word from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: None
    :rtype: None
    """
    words = fetch_words(filepath)
    print_items(words)


# fetch_words('text.txt')
if __name__ == '__main__':
    main(sys.argv[1]) # Zero index is module name
    