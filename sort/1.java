import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i =0; i<commands.length; i++){
            int a=commands[i][1]-commands[i][0]+1;
            int[] answerlist=new int[a];
            for(int j = 0; j < a; j++){
                int cnt = commands[i][0]-1;
                answerlist[j]= array[cnt+j];
            }
            Arrays.sort(answerlist);
            int n = commands[i][2]-1;
            answer[i]=answerlist[n];
        }
        return answer;
    }
}