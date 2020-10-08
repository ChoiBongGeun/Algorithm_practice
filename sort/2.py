'''
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True)
    answer = "".join(numbers)
    return answer
    str로 바꾼 다음 sort로 정렬해주었다 이렇게 하면 앞자리 숫자부터 비교해서 정렬하기 때문에 높은 숫자가 나올것이라고 생각했지만
    30,34,3같은 경우 34,3,30이 아닌 34,30,3으로 정렬해서 결과가 다르게 나왔다
'''
'''
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3 ,reverse=True)
    answer = "".join(numbers)
    return answer
    위 방법이 잘못되서 다시 문제를 보니 numbers의 원소는 1000이하라고 했기 때문에 3자리 숫자이다 
    따라서 lambda를 통해서 만약 3인 경우 333 34인 경우 343434로 만들어서 비교하였다 그렇게 하니 
    올바른 결과가 나왔으나 11번 테스트케이스에서 실패라고 떴다
'''
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*3 ,reverse=True)
    if sum(list(map(int,numbers))) == 0:
        answer = '0'
    else:
        answer = "".join(numbers)
    return answer
    #11번의 테스트 케이스의 경우를 생각해보니 [0,0,0]같은 경우 0이 나와야하는데 두번째 풀이 처럼하면 000이 나오게 된다
    #따라서 이 경우를 0으로 처리하기 위해서 전부 더했을때 0인 경우 answer를 0으로 나오게 해주었다