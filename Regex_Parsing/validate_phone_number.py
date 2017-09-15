# Validate: A valid mobile number is a ten digit number starting with a  or .
import re
for _ in range(int(raw_input())):
    input_num = raw_input()
    pattern = '([7|8|9]{1})(\d{9})$'
    print 'YES' if re.match(pattern, input_num) else 'NO'

# Sample Input:
# 2
# 9587456281
# 1252478965
