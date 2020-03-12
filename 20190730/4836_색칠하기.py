import sys
sys.stdin = open('4836_색칠하기_input.txt', 'r')

T = int(input())
for t in range(T):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    for n in range(N):
        info = list(map(int, input().split()))
        for y in range(info[1], info[3]+1):
            for x in range(info[0], info[2]+1):
                arr[y][x] += 1
    ans = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] > 1:
                ans += 1

    print('#{} {}'.format(t+1, ans))