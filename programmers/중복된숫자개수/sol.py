#(틀림)쉽게 살자...
#https://school.programmers.co.kr/learn/courses/30/lessons/120583/solution_groups?language=python3
def solution(array, n):

    answer = 0
    
    for i in array:

        if array[i] == n:
            answer += 1
        return answer


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))