 # Print their names in a specific format sorted by their age in ascending order

def person_lister(f):
    def inner(people):
        return map(f,map(lambda x: x[1],sorted(enumerate(people),key=lambda x:(int(x[1][2]), x[0]))))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))


# Sample Input:
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
