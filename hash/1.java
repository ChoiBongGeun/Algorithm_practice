import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i;
        for(i = 0; i < completion.length; i++){
            if(!participant[i].equals(completion[i])){
                answer = participant[i];
                    break;
            }
        }
        answer = participant[i];
        return answer;
    }
}
// java로 코테 연습이 필요해서 python으로 풀었던 문제를 다시 풀어 보았다 실제 풀이 방식은 python과 동일