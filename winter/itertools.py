from itertools import combinations
def solution(A, X):
    a = list(combinations(A,2))
    answer =0
    c=[]
    b = []
    for i in range(len(a)):
        n=a[i][0]*a[i][1]
        if n >= X:
            b.append([a[i][0],a[i][1]])
    while b:
        x= b[0][0]
        for i in range(len(b)):
            if b[i][0] == x:
                c.append([b[i][1],b.count(b[i][1])])
            else:
                break
        y=c[0][1]
        for i in range(len(c)):
            if c[i][1] < y:
                y = c[i][1]
                d = c[i][0]
        for i in range(len(b)):
            if d in b[i]:
                
        
    return answer
A = [5,-7,8,-2,-5,3]
X = -7
print(solution(A,X))
