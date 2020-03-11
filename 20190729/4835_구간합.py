import sys
sys.stdin = open('4835_구간합_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_sum, min_sum = 0, 10000*M
    for idx in range(N-M+1):
        test = 0
        for m in range(M):
            test += nums[idx+m]
        max_sum = max(max_sum, test)
        min_sum = min(min_sum, test)

    print('#{} {}'.format(t+1, max_sum - min_sum))