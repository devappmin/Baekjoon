package Mootata.연습.Codility;

public class CyclicRotation {
    public int[] solution(int[] A, int K) {
        int[] answer = new int[A.length];
        int len = A.length;
        if(K == len){
            return A;
        } else {
            for (int i = 0; i < len; i ++){
                answer[(i + K) % len] = A[i];
            }
        }
    return answer;
    }
}