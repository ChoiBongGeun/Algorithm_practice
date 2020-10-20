import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Map<String, String> map = new HashMap<>();
        ArrayList numberlist = new ArrayList();
        ArrayList answerlist = new ArrayList();
        int sum = 0;
        for(int i =0; i<numbers.length; i++){
            sum = sum + numbers[i];
            String str =  Integer.toString(numbers[i]);
            map.put((str+str+str),str);
            numberlist.add((str+str+str));
        }
        Collections.sort(numberlist);
        for(int i=numberlist.size()-1; i >= 0; i--){
            answerlist.add(map.get(numberlist.get(i)));
        }
        if(sum ==0){
            answer = "0";
        }
        else{
            answer = String.join("",answerlist);
        }
        return answer;
    }
}