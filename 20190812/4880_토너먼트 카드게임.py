import sys
sys.stdin = open('4880_토너먼트 카드게임_input.txt', 'r')


win_case = {1: 3, 2: 1, 3: 2}
def func(i, j):
    if i == j:
        return i
    i, j = func(i, (i+j)//2), func((i+j)//2+1, j)
    if arr[i] == arr[j] or win_case[arr[i]] == arr[j]:
        return i
    else:
        return j


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    print('#{} {}'.format(t+1, func(0, len(arr)-1)+1))