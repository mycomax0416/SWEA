import sys
sys.stdin = open('4837_부분집합의 합_input.txt', 'r')


def func(s, k):
    global subset_sum, ans

    if k == 0:
        if subset_sum == K:
            ans += 1
        return
    elif subset_sum >= K:
        return
    else:
        for num in range(s, 13):
            subset_sum += num
            func(num+1, k-1)
            subset_sum -= num


T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    subset_sum = 0
    ans = 0
    func(1, N)
    print('#{} {}'.format(t+1, ans))