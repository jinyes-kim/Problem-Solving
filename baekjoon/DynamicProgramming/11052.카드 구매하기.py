"""
점화식 세우기

0장일 때 가능한 경우 0 장
1장일 때 가능한 케이스 0장 + 1장
2장일 때 가능한 케이스 1장 + 1장, 0장 + 2장
3장일 때 가능한 케이스 1장 + 1장 + 1장, 1장 + 2장, 0장 + 3장

...

반복하면 결국 dp 구조로 반복된다.
"""

n = int(input())
pack_li = [0] + list(map(int, input().split()))
d = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + pack_li[j])

print(d[n])
