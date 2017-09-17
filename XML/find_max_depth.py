# Output a single line, the integer value of the maximum level of nesting in the XML document.

import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem._children)== 0:
        maxdepth = level + 1
    else:
        maxdepth = max([depth(child,level+1) for child in elem._children])
    return maxdepth

if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml =  xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth

# Sample Input:
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
