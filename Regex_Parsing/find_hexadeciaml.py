# Output the color codes with '#' symbols on separate lines.
import re
pattern = r':?.(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})'
is_accessible = False
for _ in xrange(int(raw_input())):
    line = raw_input()

    if '{' in line:
        is_accessible = True

    if '}' in line:
        is_accessible = False

    if is_accessible:
        r = re.findall(pattern, line)
        for match in re.findall(pattern, line, re.I):
            print match

# Sample Input:
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }
