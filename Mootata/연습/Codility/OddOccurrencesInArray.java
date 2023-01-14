package Mootata.연습.Codility;
import java.util.*;

public class OddOccurrencesInArray {
    class Solution {
        public int solution(int[] A) {
            Arrays.sort(A);
            int answer = 0;
            for (int i = 0; i < A.length; i ++){
                if(i % 2 == 0){
                    answer += A[i];
                } else {
                    answer -= A[i];
                }
            }
            return answer;
        }
    }
}
