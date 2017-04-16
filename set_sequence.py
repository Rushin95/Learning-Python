# Note:
# a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0.
# b) You can only use  sorted function in your code. A 0 score will be awarded for using sorted more than once.
# Hint: Success is not the key, but key is success.

# Enter your code here. Read input from STDIN. Print output to STDOUT
st = sorted(list(raw_input()))
oddn = filter(lambda x : x%2 == 1 ,map(int,filter(lambda x: str(x).isdigit(),st)))
evenn = filter(lambda x : x%2 == 0 ,map(int,filter(lambda x: str(x).isdigit(),st)))
lower = filter(lambda x : x.islower(),map(str,st))
upper = filter(lambda x : x.isupper(),map(str,st))
print reduce(lambda x,y: str(x)+ str(y),lower+upper+oddn+evenn)

