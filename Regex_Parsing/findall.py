# find group of vowels surrounded by 1 consonants on both the side

import re
input_str = raw_input()
ans = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',input_str)
if len(ans)!=0:
    for each in ans:
        print each
else:
    print '-1'

# Sample Input:
# rabcdeefgyYhFjkIoomnpOeorteeeeet
