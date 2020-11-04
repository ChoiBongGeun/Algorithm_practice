'''
def solution(scoville, K):
    answer = 0
    scoville.sort()
    i=0
    while True:
        if i == len(scoville):
            break
        else:
            if scoville[i] > K:
                i +=1
            else:
                scoville[i] = scoville.pop(i)+(scoville.pop(i)*2)
                scoville.sort()
                answer +=1

            
    return answer
    sort를 이용해서 풀려고 했으나 while문에 sort가 들어가니 시간초과가 떠서 다른 방법을 찾아봤다
    heapq라는 방법이 있어서 이것을 사용해서 문제를 풀었다
    '''
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #scoville를 heapq로 바꾸어주었다
    while True:
        if scoville[0] > = K:#첫번째가 가장 작은수인데 그것이 k보다 크면 while문을 나오게 했다
            break
        elif len(scoville) <= 1 and scoville[0] < K: #만약 더이상 더할게 없는데 k보다 크지 않는다면 -1이 출력되게 하였다 
            answer = -1
            break
        heapq.heappush(scoville,heapq.heappop(scoville)+(heapq.heappop(scoville)*2))         
        answer +=1

    return answer
