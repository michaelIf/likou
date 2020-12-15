# 20
# 栈
def isValid(s):
    stack = ['?']
    d = {'(': ')',
         '[': ']',
         '{': '}',
         '?': '?'}
    for i in s:
        if i in d:
            stack.append(i)
        elif d[stack.pop()] != i:
            return False
    return len(stack) == 1



