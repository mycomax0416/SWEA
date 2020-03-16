import sys
sys.stdin = open('4873_반복문자 지우기_input.txt', 'r')

T = int(input())
for t in range(T):
    words = list(input())
    
    stack = [None, None]
    for word in words:
        if word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)
    
    print('#{} {}'.format(t+1, len(stack)-2))