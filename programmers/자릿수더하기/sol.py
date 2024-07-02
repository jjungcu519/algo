
#방법2:인간적ㅋ
#def solution(result):
#
#    result = 0
#
#    for i in str(n):
#        #print(i)
        result += int(i)
#    return result
#
#print(solution(874819731))


#방법1: 수학적 ㅋ.....
# 
def solution(n):
    answer = 0

    while n > 0:
        #a: 몫, b: 나머지
        a, b = divmod(n, 10)
        
        n = answer

        answer += b

    #while(N>0):
    #    answer+=(N%10)
    #    N=N//10
    
    
    return answer


print(solution(1234))
print(solution(2930210))