"""
해당 문제는 문자열을 선택하거나 선택하지 않거나
두 개의 분기점으로 재귀가 뻗어나간다.

다시 풀어보기 좋은 문제
"""

n, m = map(int, input().split())
alphabet_li = sorted(input().split())


def check(pw):
    ja, mo = 0, 0
    for ch in pw:
        if ch in 'aeiou':
            mo += 1
        else:
            ja += 1

    return ja >= 2 and mo >= 1


def go(idx, pw):
    if len(pw) == n:
        if check(pw):
            print(pw)
        return

    if idx == len(alphabet_li):
        return

    go(idx+1, pw+alphabet_li[idx])
    go(idx+1, pw)


go(0, '')
