def solution(money):

    drinks = money // 5500
    changes = money - (5500 * drinks)
    answer = [drinks, changes]

    return answer


print(solution(5500))
print(solution(15000))