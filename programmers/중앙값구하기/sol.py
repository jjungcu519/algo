#https://centralmoo.tistory.com/entry/Programmers-LV-0-%EC%A4%91%EC%95%99%EA%B0%92-%EA%B5%AC%ED%95%98%EA%B8%B0-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC#google_vignette

def solution(array):

    array.sort()

    return array[len(array) // 2]

print(solution([9, -1, 0]))