import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        HashMap<String,Integer> hashclothes = new HashMap<String,Integer>();
        for(int i = 0; i<clothes.length; i++){
            if(hashclothes.containsKey(clothes[i][1])){
                hashclothes.put(clothes[i][1], hashclothes.get(clothes[i][1])+1);
            }
            else{
                hashclothes.put(clothes[i][1],1);
            }
        int a=1;
        for(String key : hashclothes.keySet()){ 
            a = a * (hashclothes.get(key)+1);
        }
        answer = a-1;
            
        }
        return answer;
    }
}
/*풀이 방식은 python에서 풀었던 방식 그대로 사용했다 hashmap을 만들어서 옷종류를 키로 지정했고 개수가 필요하기 때문에
키가 존재하면 +1 키가 없으면 1로 저장해주었다 그렇게 저장한 값에 없는 경우도 더해주기 위해서 +1을 해준다음 곱해주었고
전부다 안입었을경우를 빼줘야 하기 때문에 -1을 해주었다*/ 