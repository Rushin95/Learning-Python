#Validate if the given string is a roman number or not

import re
print bool(re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',raw_input().strip()))

# Sample Input:
# CDXXI
