def solution(n, k):

    answer = 0
    #n: 양꼬치 몇인분 / k: 음료수 개수
        
    
    answer = (12000 * n) + (2000 * k) - (2000 * n//10)
    
    return answer


print(solution(64,6))