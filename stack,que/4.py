def solution(priorities, location):
    answer = 0
    index1 = []
    printlist = priorities.copy()
    printlist.sort(reverse=True)
    #높은 순서대로 인쇄를 하니 sort를 이용해서 정렬해주었습니다 나중에 이거와 똑같이 priorities가 정렬되면 while문을 빠져나오기 위해
    for i in range(len(priorities)):
        index1.append(i)
    #index를 알기위해 index1이라는 리스트를 만들어 0부터 넣어주었습니다
    cnt = 0
    while True:
        if priorities[cnt] == max(priorities[cnt:]):
            cnt +=1
            #0부터 비교해서 제일 높은숫자가 맞으면 cnt올려주고 그이후에 있는리스트 부터 다시 비교 했습니다 
        else:
            priorities.append(priorities.pop(cnt))
            index1.append(index1.pop(cnt))
            #높은 숫자가 아닐경우 pop과 append를 통해서 앞에껄 빼고 뒤에껄 넣어주었습니다 index도 확인하기 위해 같이 진행
        if priorities == printlist:
            break
        #아까 sort해준 거와 priorites가 같아질 경우 정렬이 끝난것이므로 while문 빠져나옵니다
    
    print(priorities, index1,printlist)
    answer = index1.index(location)+1
    #인덱스에 저장되어있는 location위치를 찾아서 빼줍니다 0부터 시작하기 때문에 1더해서 출력
    return answer

priorities= [2, 1, 3, 2]	
location= 2

print(solution(priorities,location))