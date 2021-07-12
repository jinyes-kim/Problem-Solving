def solution(number, k):
    result = []
    
    for i, n in enumerate(number):
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        
        if k == 0:
            result += number[i:]
            break
        else:
            result.append(n)
    
    result = result[:-k] if k > 0 else result
    return ''.join(result)
            
    
