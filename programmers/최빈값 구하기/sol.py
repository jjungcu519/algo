#쉬울줄 알고 뎀볐는데ㅠㅠ
#def solution(array):
    
#    array = []
#    count = 0

#    for i in array:
#        count[i] += 1

#    return count

#print(solution([1, 2, 3, 3, 3, 4]))
#print(max([1, 2, 3, 3, 3, 4]))



def solution(array):
	count = [0] * (max(array)+1) # 숫자 출연 횟수를 셀 리스트

	for i in array:
		count[i] += 1

	m = 0 # 최빈값의 개수
	for c in count:
		if c == max(count):
			m += 1
    
	if m > 1: # 최빈값이 2개 이상이면 -1을 리턴
		return -1
	else: # 최빈값이 1개이면 해당 숫자를 리턴
		return count.index(max(count))