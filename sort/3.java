import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        for(int i = citations.length-1; i>=0; i--){
            int n = citations.length-i;
            if(n == citations[i]){
                answer=n;
                break;
            }
            else if(n > citations[i]){
                answer = n-1;
                break;
            }
            else{
                answer =citations.length;
            }
        }
        return answer;
    }
}