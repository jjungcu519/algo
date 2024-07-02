# replace 활용
# def solution(my_string, letter):
#    answer = ''
#    return answer


def solution(my_string, letter):
    return(my_string.replace(letter,''))

    # answer = my_string.replace(letter,'')

print(solution('asdtyudef','de'))


##방법2:

#def solution(my_string, letter):
#    answer = ''
#
#    for char in my_string
#        if char != letter:
#            answer += char
#    return answer