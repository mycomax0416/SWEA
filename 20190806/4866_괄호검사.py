import sys
sys.stdin = open('4866_괄호검사_input.txt', 'r')

T = int(input())
for t in range(T):
    words = list(input())

    stack = [0]
    for word in words:
        if word == '(' or word == '{' or word == ')' or word == '}':
            stack.append(word)
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
            elif stack[-2] == '{' and stack[-1] == '}':
                stack.pop()
                stack.pop()
    if stack == [0]:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))    