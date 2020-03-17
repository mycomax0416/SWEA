import sys
sys.stdin = open('4881_배열 최소 합_input.txt', 'r')


def func(val, y):
    global min_val
    if val >= min_val:
        return
    elif y == N:
        min_val = min(min_val, val)
        return
    else:
        for x in range(N):
            if visit[x] == False:
                visit[x] = True
                func(val+arr[y][x], y+1)
                visit[x] = False


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = [False for _ in range(N)]
    min_val = 10 * N
    func(0, 0)

    print('#{} {}'.format(t+1, min_val))