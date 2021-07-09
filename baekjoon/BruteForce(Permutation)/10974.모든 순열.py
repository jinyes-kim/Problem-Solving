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
permutation_li = [x for x in range(1, n+1)]

print(' '.join(map(str, permutation_li)))
while next_permutation(permutation_li):
    print(' '.join(map(str, permutation_li)))
