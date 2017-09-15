# Find the index of matched substring including the OVERLAPPING SUBSTRINGS

import re

input_str, pattern = raw_input(), raw_input()
ans = [(result.start(1), result.end(1) - 1) for result in re.finditer(r'(?=(%s))' % pattern, input_str)]
if len(ans)==0:
    print (-1,-1)
else:
    for each in ans:
        print each

# Sample Input:
# aaadaa
# aa
