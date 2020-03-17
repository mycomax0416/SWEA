import sys
sys.stdin = open('1221_GNS_input.txt', 'r')

T = int(input())
for _ in range(T):
    t, N = input().split()
    arr = list(input().split())

    ans = []
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for num in nums:
        for test in arr:
            if test == num:
                ans.append(num)

    print('{} \n{}'.format(t, ' '.join(ans)))