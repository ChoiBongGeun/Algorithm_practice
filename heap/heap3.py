def solution(operations):
    answer = []
    operationslist=[] #숫자를 넣어주고 빼줄 리스트 하나 생성
    for i in range(len(operations)):
        operation=operations[i].split(' ')#operation을 그냥 operations[i][0]이런식으로 진행할려니 -가 붙을시 하나씩 늘어나는것이 힘들어서 split해주었다
        if operation[0] == 'I':
            operationslist.append(int(operation[1]))
        elif operationslist:
            if operations[i] == 'D -1':#전체를 보는것이 더 편한듯 해서 그냥 operations[i]로 해주었다
                operationslist.remove(min(operationslist))#-1이기 때문에 최소값제거
            else:
                operationslist.remove(max(operationslist))#아닌 경우는 D 1밖에 없기 때문에 최대값 제거
        else:
            continue
    if not operationslist: #위에 정돈된 리스트가 비었을시 0,0을 answer에 입력
        answer =[0,0]
    else:
        answer = [max(operationslist),min(operationslist)] #아닌경우 max와 min을 찾아서 정렬해준다
    return answer
