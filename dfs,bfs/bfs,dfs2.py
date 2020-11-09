def dfs(computers,v,s):
    start =[]
    start.append(s)#시작점을 start리스트에 넣어주기
    while start:
        number = start.pop()
        if v[number] == 0: #방문한 리스트가 0이면 이번에 방문하므로 1로 바꾸어주기
            v[number] = 1
        for i in range(len(computers[0])):
            if i != number and computers[number][i] == 1 and  v[i] == 0: 
                #i와 number가 같으면 무조건 1이므로 제외 computer[number][i]가 1이면 네트워크가 존재,방문한곳은 방문하지 않게 0인곳만 방문
                start.append(i)#start리스트에 넣어주고 반복한다 리스트에 아무것도 없을때까지
                          
def solution(n, computers):
    answer = 0
    v=[0] *n #어디 방문한지를 알기위해서 컴퓨터 수만큼 0으로 된 리스트를 생성
    s = 0 #0부터 시작
    while 0 in v:
        if v[s] == 0:#0이면 아직 방문하지 않은곳이기 때문에 dfs로 네트워크 확인 1일경우 이미 방문했으므로 패스
            dfs(computers,v,s)
            answer +=1
        s+=1
                
    return answer