def solution(numbers):
    
    result = []

    for number in numbers:
        result.append(number * 2)

    return result

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))

