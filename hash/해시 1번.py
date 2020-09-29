# set으로 바꾼 다음 풀려고 했으나 동명이인 선수가 있을시 set은 중복을 제거하므로 찾을 수 없었다

'''
def solution(participant, completion):
    answer = ''
    a=[]
    a = list(set(participant)-set(completion))
    answer = a[-1]
    return answer
'''
#두 리스트를 sort를 이용하여 순서대로 만든뒤 앞에서 부터 비교 하여 만약 다를 경우 그애는 완주하지 못했다고 간주해서 answer에 저장하고 break로 빠져나온다
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
#for문을 다 돌았는데 answer가 정해지지 않은 경우는 participant마지막에 있는 선수가 완주하지 못한것이므로 마지막을answer에 저장한다
    if answer == '':
        answer = participant[-1]
        
    return answer
