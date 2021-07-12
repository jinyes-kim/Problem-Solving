def solution(citations):
    length = len(citations)
    citations.sort()
    
    for i in range(length):
        if citations[i] >= length-i:
            return length-i
    return 0