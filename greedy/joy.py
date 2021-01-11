def solution(name):
    answer = 0
    name = list(name)
    alpa=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #a~z까지 몇번 바꾸는지 알기위해서 리스트 작성 
    #전부 A로 되어있기 때문에 A는 리스트로 봤을때 0이 되므로 A를 포함한 리스트 작성
    i = 0
    while True:
        print(i)
        right = 1
        left = 1
        if name[i] != 'A': #A가 아닌경우만 한 이유는 전부 A가 되면 break로 while문 탈출을 위해 작성
            if alpa.index(name[i]) >13:
                answer= answer+len(alpa)-alpa.index(name[i])
            else:
                answer +=alpa.index(name[i])
        name[i] = "A"#while 탈출을 위해 찾은 단어는 A로 변형
        if name == ["A"]*len(name): #전부 A가 되면 탈출
            break

        for j in range(1,len(name)):#오른쪽으로 갔을때 A가 연속으로 몇개 있는지 확인
            if name[i+j]=="A": 
                right+=1
            else: 
                break
        for j in range(1,len(name)):#왼쪽으로 갔을때 A가 연속으로 몇개 있는지 확인
            if name[i-j]=="A": 
                left+=1
            else: 
                break
        if right>left:#라이트가 더 많으면 왼쪽으로 이동 i가 음수면 자동으로 끝에서 부터 이동 하므로상관없습니다
            answer+=left
            i-=left
        else:
            answer+=right
            i+=right
    return answer

name = "ABAAAAABAB"
print(solution(name))
            