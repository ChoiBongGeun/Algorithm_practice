import math

def solution(w,h):
    answer = w*h - (w+h-math.gcd(w,h))    
    return answer
#전체 사각형 넓이에서 w+h한다음 w,h최소공배수를 구하면 답을 구할수 있다