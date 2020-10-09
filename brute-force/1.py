def solution(answers):
    answer = []
    result=[]
    p=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    cnt = 0
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == p[i][j%len(p[i])]:
                cnt += 1
        if cnt >0:
            result.append([cnt,i+1])
            cnt = 0
    result.sort(key=lambda x:x[0], reverse=True)
    for i in range(len(result)):
        if result[i][0] == result[0][0]: 
            answer.append(result[i][1])
    return answer

