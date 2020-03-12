import sys
sys.stdin = open('4839_이진탐색_input.txt', 'r')


def func(l, r, end, cnt):
    c = (l+r)//2
    if c == end:
        print(cnt+1)
        return 2
    elif end < c:
        func(l, c, end, cnt+1)
    else:
        func(c, r, end, cnt+1)


T = int(input())
for t in range(1):
    P, Pa, Pb = map(int, input().split())

    # print(func(1, P, Pa, 0))
    A = func(1, P, Pa, 0)
    # B = func(1, P, Pb, 0)
    print(A)

    # if A < B:
    #     ans = A
    # elif A == B:
    #     ans = 0
    # else:
    #     ans = B

    # print('#{} {}'.format(t+1, ans))