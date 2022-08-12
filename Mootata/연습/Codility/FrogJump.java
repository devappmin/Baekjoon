package Mootata.연습.Codility;

public class FrogJump {
    public static int solution(int X, int Y, int D) {
        int num = (int) Math.ceil(((double)(Y - X) / D));
        return num;
    }
}