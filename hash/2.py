def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book[0])
    for i in range(1,len(phone_book)):
        if phone_book[0] == phone_book[i][:n]:
            answer = False   
    return answer

#phone_book을 sort를 이용하여 작은수 즉 자릿수가 가장 작은 순서대로 재배치후 phone_book에서 첫번째와 다른 번호들은 앞에서 부터 첫번째 자리수 만큼 자른후 두 숫자를 비교해보는 식으로 코드를 작성했다

'''
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
'''
#다 풀고 다른 사람 풀이를 봤는데 startswith을 사용하면 더 편리하게 문제를 해결할 수 있다 startswith은 접두어를 확인하기 때문에 startswith을 사용하면 더편리하다 