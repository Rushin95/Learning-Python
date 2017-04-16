'''
Write a function answer(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.
><>s
Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4

'''

l = "<<>><"
salute = 0
for i in range(len(l)):
    if l[i] == '>':
        salute += l[i+1:len(l)].count('<')
    elif l[i] == '<':
        salute += l[0:i+1].count('>')
print 'no of salute:',salute

