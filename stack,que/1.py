def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer

#가격비교를 위해서 숫자를 비교하였다 비교해서 만약 자신보다 작은숫자가 나온순간 brak를 통해서 나오고 몇번만에 작은수가 나온지 체크한다
#마지막 숫자는 비교할 필요가 없기 때문에 마지막 전까지만 for문이 돌아가게 하였다