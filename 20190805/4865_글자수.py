import sys
sys.stdin = open('4865_글자수_input.txt', 'r')

T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()

    words = set(str1)
    words_cnt = dict()
    for word in str2:
        if word not in words_cnt:
            words_cnt[word] = 1
        else:
            words_cnt[word] += 1
    ans = 0
    for word in words:
        if word in words_cnt:
            ans = max(ans, words_cnt[word])

    print('#{} {}'.format(t+1, ans))