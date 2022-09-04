package Mootata.연습.Codility;
public class BinaryGap {
    public static void main(String args[]){
        int answer = 0;
        int count = 0;
        String bS = Integer.toBinaryString(15);
        String[] list = bS.split("");
        for(String s : list){
            if(s.equals("0")){
                count ++;
            } else {
                answer = Math.max(answer, count);
                count = 0;
            }
        }
        System.out.println(answer);
    }
}
