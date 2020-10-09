def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 == citations[i]:
            answer = i+1
            break
        elif i+1 > citations[i]:
            answer = i
            break
        else:
            answer = len(citations)
    return answer
    
#처음에 h-index계산법을 몰라서 고민했으나 문제에 써있는 위키를 참고해서 풀었다 
#3가지 경우가 있으며 높은 순서대로 정렬한뒤 i번째와 i+1이 같으면 i+1
#두번째 i+1이 i번째보다 큰수이면 i 마지막으로 두경우 다 아니면 citation의 배열 크기이다