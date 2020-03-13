import sys
sys.stdin = open('4864_문자열 비교_input.txt', 'r')

T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()

    ans = 0
    if str1 in str2:
        ans = 1

    print('#{} {}'.format(t+1, ans))