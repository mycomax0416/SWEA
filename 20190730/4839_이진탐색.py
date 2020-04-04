import sys
sys.stdin = open('4839_이진탐색_input.txt', 'r')


def func(l, r, end, cnt):
    c = (l+r)//2
    if c == end:
        return cnt+1
    elif end < c:
        return func(l, c, end, cnt+1)
    else:
        return func(c, r, end, cnt+1)


T = int(input())
for t in range(T):
    P, Pa, Pb = map(int, input().split())

    A = func(1, P, Pa, 0)
    B = func(1, P, Pb, 0)

    if A < B:
        ans = 'A'
    elif A == B:
        ans = 0
    else:
        ans = 'B'

    print('#{} {}'.format(t+1, ans))