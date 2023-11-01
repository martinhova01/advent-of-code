package day9;

import util.InputReader;

public class Main {
    
    public static void main(String[] args) {
        String input = InputReader.getInput("../day9/input.txt");
        SnakeP1 snakeP1 = new SnakeP1();
        SnakeP2 snakeP2 = new SnakeP2();

        for (String line : input.split("\n")){
            char direction = line.split(" ")[0].charAt(0);
            int number = Integer.parseInt(line.split(" ")[1]);

                //part 1
            snakeP1.moveHead(direction, number);

                //part 2
            for (int i = 0; i < number; i++){
                snakeP2.moveHead(direction);
            }
        }

        System.out.println("Part1 : " + snakeP1.getVisitedPositions().size());
        System.out.println("part 2 : " + snakeP2.getNumberOfVisitedPositions());
    }
}
