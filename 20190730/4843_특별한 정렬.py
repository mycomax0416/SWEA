import sys
sys.stdin = open('4843_특별한 정렬_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    
    ai.sort()
    ans = []
    for _ in range(5):
        ans.append(str(ai.pop()))
        ans.append(str(ai.pop(0)))
    
    print('#{} {}'.format(t+1, ' '.join(ans)))