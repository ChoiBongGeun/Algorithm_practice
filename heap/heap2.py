def solution(jobs):
    answer = 0
    time= 0
    n = len(jobs) #나중에 평균을 구하기 위해 전체 몇개가 존재한지 저장해준다
    jobs.sort(key=lambda x: x[1])#소요되는 시간으로 정렬시킨다
    while True:
        if len(jobs) ==0: #pop을 통해 언제 break할지를 정해준다
            break
        else:
            for i in range(len(jobs)):
                if jobs[i][0] <= time: #소요시간이 작은되로 정렬했으니 만약 시간이 같거나 작은 것이 있으면 바로 넣어준다
                    time += jobs[i][1]
                    answer += time - jobs[i][0]
                    jobs.pop(i)
                    break
                elif i == len(jobs) - 1:#끝까지 됬는데 만약 시간이 같거나 작은것이 없었다면 시간을 1늘려준다
                    time +=1
                else:
                    continue

    answer = answer //n
    return answer



jobs=[[2,10],[1,9],[2,6]]
print(solution(jobs))