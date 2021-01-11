import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        Map<String,Integer> players = new HashMap<>();
        ArrayList<genreslist> playlist=new ArrayList<>();
        for(int i =0; i<genres.length; i++){
            if(players.containsKey(genres[i])){
                players.put(genres[i],players.get(genres[i])+plays[i]);
                playlist.add(genres[i],plays[i],i);
            }
            else{
                players.put(genres[i],plays[i]);
                playlist.add(new generslist(genres[i],plays[i],i));
            }
        }
        return answer;
    }
}