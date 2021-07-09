"""
1. 순열 제일 뒤 인덱스를 i에서 시작해서 i-1 >= i이 되는 시점 찾기
2. 순열의 제일 뒤에서부터 해당 인덱스의 숫자보다 처음으로 커지는 인덱스와 스왑
3. 1번에서 찾은 인덱스 다음부터 양쪽 끝에서 투 포인터 정렬
"""


def next_permutation(permu_li):
    i = j = len(permu_li)-1
    while i > 0 and permu_li[i-1] >= permu_li[i]:
        i -= 1
    if i <= 0:
        return False

    while permu_li[j] <= permu_li[i-1]:
        j -= 1

    permu_li[i-1], permu_li[j] = permu_li[j], permu_li[i-1]
    j = len(permu_li)-1
    while i < j:
        permu_li[i], permu_li[j] = permu_li[j], permu_li[i]
        i += 1
        j -= 1

    return True


n = int(input())
permutation_li = list(map(int, input().split()))
if next_permutation(permutation_li):
    print(' '.join(map(str, permutation_li)))
else:
    print(-1)
    