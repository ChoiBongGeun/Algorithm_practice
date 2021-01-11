import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int[] p1 = new int[] {1,2,3,4,5};
        int[] p2 = new int[] {2,1,2,3,2,4,2,5};
        int[] p3 = new int[] {3,3,1,1,2,2,4,4,5,5};
        int[] answerlist = new int[3];
        int[] list = new int[3];
        for(int i = 0; i < answers.length; i++){
            if(answers[i] == p1[i%p1.length]){
                answerlist[0] +=1;
                list[0]+=1;
            }
            if(answers[i] == p2[i%p2.length]){
                answerlist[1] += 1;
                list[1]+=1;
            }
            if(answers[i] == p3[i%p3.length]){
                answerlist[2] += 1;
                list[2]+=1;
            }
        }
        
        Arrays.sort(answerlist);
        int max = answerlist[2];
        if(max ==0) {
        	return new int[] {0};
        }
        else{
            for(int i = 0; i < list.length; i++){
                if (max == list[i]){
                answer.add(i+1);
                
            }
        }
        int[] ans = new int[answer.size()];
        for (int i = 0; i < ans.length; ++i) {
            ans[i] = answer.get(i);
        }

        return ans;
        }
    }
}