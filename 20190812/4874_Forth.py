import sys
sys.stdin = open('4874_Forth_input.txt', 'r')

T = int(input())
for t in range(T):
    texts = list(input().split())

    stack = []
    ans = 0
    for text in texts:
        if text.isdigit():
            stack.append(int(text))
        elif text == '+' and len(stack) > 1:
            stack.append(stack.pop(-2)+stack.pop())
        elif text == '-' and len(stack) > 1:
            stack.append(stack.pop(-2)-stack.pop())
        elif text == '*' and len(stack) > 1:
            stack.append(stack.pop(-2)*stack.pop())
        elif text == '/' and len(stack) > 1:
            stack.append(stack.pop(-2)//stack.pop())
        elif text == '.' and len(stack) == 1:
            ans = stack[0]
        else:
            ans = 'error'
            break

    print('#{} {}'.format(t+1, ans))