#내가 푼거 아님, 분하다.
def solution(my_string, n):
    
    #my_string = '' (왜 이게 있으면 안될까?ㅠㅠ)
    answer = ''  
    
    for s in my_string:
        answer += s*n
    #print(my_string[1])

    return answer


print(solution('hello', 3))