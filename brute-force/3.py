def solution(brown, yellow):
    answer = []
    n = brown + yellow #전체 넓이
    for i in range(1,n+1):
        if n%i == 0:#전체 넓이 가로 또는 세로 길이 구하기 위해 나머지가 0인수 찾기
            l=n//i#위에껄 가로로 가정하면 세로 찾기
            if (i-2)*(l-2)==yellow :#문제에서 원하는 가로 세로길이를 위해 가로와 세로 길이를 2씩 빼주고 곱하면 노란색타일의 넓이가 나온다
                answer=[i,l]#그렇게 찾은수 answer에 넣어주기
                answer.sort(reverse = True)#가로의 길이가 무조건 더 길거나 같다는 제한조건이 있으므로 sort로 정렬시켜준다
                break#나머지는 계산할 필요 없으니 break
            else:
                continue
        else:
            continue
    return answer