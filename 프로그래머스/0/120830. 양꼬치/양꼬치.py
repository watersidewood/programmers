def solution(n, k):
    yang = n * 12000
    k -= n // 10
    can = k * 2000
    answer = yang + can
    
    return answer