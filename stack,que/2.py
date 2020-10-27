def solution(progresses, speeds):
    answer = []
    answerlist = []
    for i in range(len(progresses)):
        cnt = 0
        pro = progresses[i]
        while(pro < 100):
            pro= pro + speeds[i]
            cnt +=1
        answerlist.append(cnt)
    #progresses랑 speeds를 더해줘서 100이 안넘으면 계속해서 speeds를 더해줄수 while을 이용했다 더할때 마다 cnt를 1씩 추가해 날짜를 카운트해줬다
    idx = 0
    for i in range(len(progresses)):
        if answerlist[idx] < answerlist[i]:
            answer.append(i-idx)
            idx = i
    answer.append(len(progresses)-idx)
    #for 문을 이용하여 첫번째와 비교하여 작은 수가 나올때 까지 비교한다음 작은수가 나오면 i-idx를 하여 날짜를 세워주고 idx를 i로 바꾸어서 반복한다
    #마지막까지 돌렸을때 남은 것들은 전부 idx보다 작으므로 같은 날짜에 배포된다 따라서 전체수에 idx를 빼준다음 answer에 넣어주었다 
    return answer
