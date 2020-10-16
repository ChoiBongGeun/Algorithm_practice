/*
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        int n = phone_book[0].length();
        for(int i = 1; i < phone_book.length; i++){
            if(phone_book[0].equals(phone_book[i].substring(0,n))){
                answer = false;
                break;
            }
        }
        return answer;
    }
}
sort를 해서 정렬을 한뒤 phone_book 제일 앞에있는 번호가 다른 번호 접두어인지 substring을 통해서
확인해주었는데 몇개의 테스트 케이스에서 런타임에러가 나서 startSwith으로 바꾸어서 해결하였다
런타임 오류 이유로는 '111111' '87' 같은 경우 사전적으로 sort하기 때문에 87,11111이 아니라 
111111,87로 정렬되기 때문이다
*/

import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        int n = phone_book[0].length();
        for(int i = 1; i < phone_book.length; i++){
            if(phone_book[i].startsWith(phone_book[0])){
                answer = false;
                break;
            }
        }
        return answer;
    }
}