import sys
sys.stdin = open('5099_피자 굽기_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    for m in range(M):
        pizza.append((m+1, pizza.pop(0)))
    oven = [pizza.pop(0) for _ in range(N)]
    while len(oven) != 1:
        n, C = oven.pop(0)
        if C != 1:
            oven.append((n, C//2))
        else:
            if pizza:
                oven.append(pizza.pop(0))

    print('#{} {}'.format(t+1, oven[0][0]))