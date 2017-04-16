from itertools import groupby

lines = '''
this is the first paragraph.

this is the second.

'''.splitlines()

for has_chars,frags in groupby(lines,bool):
    if has_chars:
        print ' '.join(frags)
