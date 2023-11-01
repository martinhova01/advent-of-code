package day10;

import util.InputReader;

public class Main {
    
    public static void main(String[] args) {
        String input = InputReader.getInput("../day10/input.txt");
        Register x = new Register();

        for (String line : input.split("\n")) {
            if(line.equals("noop")){
                x.noop();
            }
            else if (line.startsWith("add")){
                int value = Integer.parseInt(line.substring(5));
                x.add(value);
            }
        }

            //part 1
        System.out.println(x.getlistener().getSignalStrength());

            //part 2
        System.out.println(x.getlistener().getDrawing());
    }
}
