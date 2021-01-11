/*
class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int a = w;
        int[] answerlist = new int[n];
        for(int i =0; i <stations.length; i++){
            while(w !=0){
                if(stations[i]+w-1 > n){
                    break;
                } 
                else{
                    answerlist[stations[i]+w-1] = 1;
                    w--;
                }
            }
            answerlist[stations[i]-1] = 1;
            w =a;
            while(w !=0){
                if(stations[i]-w-1 < 0){
                    break;
                } 
                else{
                    answerlist[stations[i]-w-1] = 1;
                    w--;
                }
            }
        }
        int b = 0;
        for(int i =0; i< n; i++){
            if(answerlist[i] ==0 && b !=3){
                b++;
            }
            else if (b!=0 && answerlist[i]==1){
                answer++;
                b = 0;
            }
            else if (b==3){
                answer++;
                b = 1;
            }
        }
        

        return answer;
    }
}
효율성 빵점 다시 풀기 ㅠㅠ
*/