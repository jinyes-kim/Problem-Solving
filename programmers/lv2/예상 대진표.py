def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        
        if a == b:
            return answer
        else:
            a //= 2
            b //= 2

    return answer