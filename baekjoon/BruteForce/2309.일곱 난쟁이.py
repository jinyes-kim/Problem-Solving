def search(dwarf_list):
    total = sum(dwarf_list)
    length = len(dwarf_list)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if total - (dwarf_list[i] + dwarf_list[j]) == 100:
                return i, j


dwarf_list = [int(input()) for _ in range(9)]
dwarf_list.sort()
result = []
i, j = search(dwarf_list)

for x in range(len(dwarf_list)):
    if x == i or x == j:
        continue
    result.append(dwarf_list[x])

print(*result, sep='\n')
