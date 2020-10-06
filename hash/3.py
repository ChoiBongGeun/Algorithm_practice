clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
def solution(clothes):
    answer = 1
    setc={}
    for i in clothes:
        value = i[0]
        key = i[1]
        if key in setc:
            setc[key] +=1
        else:
            setc[key]= 1

    for i in setc.keys():
        print(setc[key],key)
        answer =answer*(int(setc[key])+1)
        
    return answer-1
    
    
print(solution(clothes))
