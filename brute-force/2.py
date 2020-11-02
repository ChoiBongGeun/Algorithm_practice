'''
def solution(numbers):
    answer = 0
    numberlist = list(numbers)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                numberlist.append(numberlist[i]+numberlist[j])
            else:
                continue
    for i in range(len(numberlist)):
        if primenumber(int(numberlist[i])):
            answer +=1
        else:
            continue
    return answer
만들어지는 수를 위하여 numbers를 리스트로 만들어준다음 합쳐줬는데 저렇게 하면 1,2,3이 213이 되는 경우를 만들수 없었다
찾아보니 itertools를 import시켜서permutations를 사용하면 되는것을 알게 되었다 
'''
import itertools
def solution(numbers):
    answer = 0
    numberlist=[]
    for i in range(1,len(numbers)+1):
        number = list(itertools.permutations(numbers,i)) 
        for j in number:
            number = "".join(j)
            numberlist.append(int(number))#처음에 int로 안만들어주고 구했으나 그렇게 하면 011과 11을 다르게 판단하여 중복으로 구하여서 int로 저장해주었다
    numberlist=list(set(numberlist))#중복을 지우기 위해 set을 한다음 다시 리스트로 만들어주었다 순서는 상관없기 때문에 사용할수 있던 방법
    for i in range(len(numberlist)):
        if primenumber(numberlist[i]):
            answer +=1
        else:
            continue
    return answer
#소수 구하는 함수를 작성하였다 0,1은 무조건 소수가 아니라고 판단하고 2부터는 자기자신을 제외하고 나눠지는 수가 있는지 확인하였다   
def primenumber(n):
    if n !=1 and n!=0:
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                continue
    else:
        return False
    return True