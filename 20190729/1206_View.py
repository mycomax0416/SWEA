import sys
sys.stdin = open('1206_View_input.txt', 'r')

for t in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for n in range(N-4):
        test = list()
        for m in range(5):
            test.append(arr[n+m])
        mid = test.pop(2)
        if max(test) < mid:
            ans += mid - max(test)

    print('#{} {}'.format(t+1, ans))