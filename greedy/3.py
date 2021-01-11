def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    answerlist=[0]*n
    print(n)
    for i in range(n):
        if answerlist[costs[i][0]] ==0:
            answerlist[costs[i][0]] =1
            answer+=1
        if answerlist[costs[i][1]] ==0:
            answerlist[costs[i][1]] =1
            answer+=1
    return answer

n = 4
costs=	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))