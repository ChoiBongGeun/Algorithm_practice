'''
def solution(generes, plays):
    answer = []
    players=[]
    playlist={}

    for i, p in zip(generes,plays):
        players.append([i,p])
    for i in range(len(players)):
        if players[i][0] in playlist:
            playlist[players[i][0]].append([players[i][1],i])
            playlist[players[i][0]].sort(reverse=True)
        else:
            playlist[players[i][0]] = [[players[i][1],i]]
    maxvalue=[]
    for i in playlist:
        maxvalue.append([playlist[i][0][0],i])
    maxvalue.sort(reverse=True)
    for i in range(len(maxvalue)):
        if len(playlist[maxvalue[i][1]]) > 1:
            answer.append(playlist[maxvalue[i][1]][0][1])
            answer.append(playlist[maxvalue[i][1]][1][1])
        else:
            answer.append(playlist[maxvalue[i][1]][0][1])
    return answer
    오류가 났던 이유로는 문제를 제대로 읽지 않아서 장르별 총합을 신경쓰지 않고 장르별중 가장 큰수만 비교했기 때문이다 그렇기 때문에
    장르별 총합을 추가해주면서 코드 또한 필요하지 않는 부분이 보여 고쳐주었다
'''

def solution(generes, plays):
    answer = []
    playlist={}
    maxvalue={}

    for i in range(len(generes)):
        if generes[i] in playlist:
            playlist[generes[i]].append([plays[i],i])
            maxvalue[generes[i]] =maxvalue[generes[i]]+plays[i]
            #playlist[generes[i]].sort(reverse=True) 이렇게 작성하니 같은 장르에서 똑같이 들었을 경우 앞에 고유 숫자 순으로 배치 하기 때문에 뒤에 나온 고유 번호가 answer에 먼저 들어가는 오류가 있었다
            playlist[generes[i]].sort(key = lambda x: x[0], reverse=True)
            #위에 오류를 방지하기 위해 sort를 들은 숫자로만 하게 lambda를 설정해주었다
        else:
            playlist[generes[i]] = [[plays[i],i]]

            maxvalue[generes[i]] = plays[i]
    maxvaluesorted = sorted(maxvalue.items(), key=lambda x: x[1], reverse=True) 
    for i in range(len(playlist)):
        if len(playlist[maxvaluesorted[i][0]]) > 1:
            answer.append(playlist[maxvaluesorted[i][0]][0][1])
            answer.append(playlist[maxvaluesorted[i][0]][1][1])
        else:
            answer.append(playlist[maxvaluesorted[i][0]][0][1])

    return answer
