import sys
sys.stdin = open('5097_회전_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for m in range(M):
        arr.append(arr.pop(0))

    print('#{} {}'.format(t+1, arr[0]))