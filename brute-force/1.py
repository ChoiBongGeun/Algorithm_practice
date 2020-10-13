def solution(answers):
    answer = []
    result=[]
    p=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    #p에 수포자1,수포자2,수포자3이 찍는 규칙성을 찾은뒤 리스트에 넣어 주었다
    cnt = 0
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == p[i][j%len(p[i])]:
                cnt += 1
            #정답 맞힌 횟수를 cnt에 넣어 주었으며 규칙적으로 답을 적기 때문에 문제 번호 나누기 리스트의 길이를 하면 문제에 맞는 찍는 순서가 나온다
        if cnt >0:
            result.append([cnt,i+1])
            cnt = 0
        #그렇게 해서 맞은 개수가 0이 아니면 맞은 개수와 함께 수포자1,2,3,인지를 저장해준다
    result.sort(key=lambda x:x[0], reverse=True)
    #개수가 많은 수대로 정렬해준다
    for i in range(len(result)):
        if result[i][0] == result[0][0]: 
            answer.append(result[i][1])
            #맞은개수가 같을수도 있기 때문에 가장 많이 맞은 개수와 같은 즉 동점인 애들을 answer에 차례대로 저장한다
    return answer

