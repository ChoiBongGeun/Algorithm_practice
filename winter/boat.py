def solution(people, limit):
    answer = 0
    people.sort(reverse = True)#큰수 부터 차례대로 정렬했다
    i = 0
    j = len(people)-1
    while i <= j:
        answer +=1
        if people[i]+people[j] > limit: #제일큰수와 작은수를 더했을때 리미트 보다 크면 큰수를 보내고 다음 큰수와 작은수를 비교하였다
            i +=1
        else:#리미트보다 작을 경우 큰수와 작은수를 보내고 다음 큰수와 다음 작은수를 비교하였다
            i+=1
            j-=1
    return answer

'''
people=[70, 50, 80]
limit = 100
print(solution(people,limit))
'''