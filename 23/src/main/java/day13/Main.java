package day13;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String input = InputReader.getInput("testinput.txt");

        String[] pairs = input.split("\n\n");

        List<Integer> indicies = new ArrayList<>();

        for (int i = 0; i < pairs.length; i++){
            String pair = pairs[i];
            Packet p1 = new Packet(pair.split("\n")[0]);
            Packet p2 = new Packet(pair.split("\n")[1]);

            if (p1.compareTo(p2) < 1){
                indicies.add(i + 1);
            }
        }

        System.out.println(indicies);
    }
    
}
