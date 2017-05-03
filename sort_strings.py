'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

INPUT:
superman,batman,spiderman,flash,captain,hulk

OUTPUT
batman,captain,flash,hulk,spiderman,superman
'''
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)