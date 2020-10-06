def solution(clothes):
    answer = 1
    setc={}
    #부위별 옷이 몇개 있는지 숫자를 세어서 넣어 준다 
    for i in clothes:
        value = i[0]
        key = i[1]
        if key in setc:
            setc[key] +=1
        else:
            setc[key]=1

    for i in setc.keys():
        answer =answer*(int(setc[i])+1)
        #하나 이상의 부위를 착용가능하기 때문에 착용하지 않는것도 확률에 넣어야한다 그렇기 때문에 +1을 해준다음 곱해준다 
        #이럴경우 전부 착용하지 않는 경우도 있기 때문에 총합에서 그경우를 빼주면 된다
    return answer-1


'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
굳이 위에 방법처럼 해쉬로 만들지 않고 counter를 이용하여 구하는 방식인 이 방법이 더 낮다고 생각한다 
위 문제를 풀 당시에는 생각하지 못했던 방법
'''