def solution(n):
    answer = ''
    while True:
        if n <=3:
            answer = '124'[n-1]+answer
            break
        else:
            n,y =divmod(n-1,3)
            answer = '124'[y]+answer
    return answer

#3진법 푸는 방식으로 풀었으며 0,1,2 대산 1,2,4가 나오게 했습니다