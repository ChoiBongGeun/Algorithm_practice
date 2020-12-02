def solution(number, k):
    answer = ''
    answerlist = []
    for i in range(len(number)):
        while len(answerlist) > 0 and answerlist[-1] < number[i] and k > 0: #answerlist에 아무것도 없거나 새로 들어오는 숫자가 더크거나 뺄게 더 있다면 실행
            k -= 1 #하나 뺐으니 k에 -1
            answerlist.pop()
        answerlist.append(number[i])
    if k != 0:#다 들어갔는데 k가 아직 0이 아니면 뒤에부터 순서대로 제거
        answerlist = answerlist[:-k]
    answer =''.join(answerlist)
    return answer



#테스트용 

number='1231234'
k = 3
print(solution(number,k))