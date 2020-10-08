def solution(array, commands):
    answer = []
    lista=[]
    
    for i in range(len(commands)):
        for j in range(commands[i][0]-1,commands[i][1]):
            lista.append(array[j])
        #lista를 새로 만들어 준 뒤 range를 통해 넣어주었다 여기서 list는 0부터 시작하기 때문에 앞부분에 -1을 해주었다
        lista.sort()
        answer.append(lista[commands[i][2]-1])
        del lista[:]    
        #그렇게 해서 찾은 다음 lista를 다시 비워준 후 이것을 반복하는 방식으로 문제를 풀었다
    return answer

'''
 def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
단 두줄로 문제를 풀수 있다는것도 놀랐지만 제가 생각보다 lambda를 잘 활용하지 못한다는것을 느꼈다 lambda에 대해 좀 더 공부하기  
'''  
