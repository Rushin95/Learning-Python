# Substitute && and || with and,or
import re
for _ in range(int(raw_input())):
    print re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', raw_input())

'''
for _ in range(int(raw_input())):
    line = raw_input()
    line = re.sub(r'(?<= )(&&)(?= )','and',line)
    line = re.sub(r'(?<= )(\|\|)(?= )','or',line)
    print line
'''

# Sample Input:
# 11
# a = 1;
# b = input();
#
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
