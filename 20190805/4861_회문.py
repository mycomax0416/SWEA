import sys
sys.stdin = open('4861_회문_input.txt', 'r')


def func():
    for y in range(N):
        for x in range(N-(M-1)):
            test = []
            for m in range(M):
                test.append(arr[y][x+m])
            if test == test[::-1]:
                print(''.join(test))


def arr_dia():
    for y in range(N):
        for x in range(y, N):
            arr[y][x], arr[x][y] = arr[x][y], arr[y][x]


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print('#{}'.format(t+1), end=' ')
    func()
    arr_dia()
    func()