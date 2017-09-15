# Parse and validate email
import re
import email.utils
for _ in range(int(raw_input())):
    line = raw_input()
    name, emailid = email.utils.parseaddr(line)
    pattern="[a-zA-Z]{1}[a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    if bool(re.match(pattern,emailid)): print line

# Sample Input:
# 2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>
