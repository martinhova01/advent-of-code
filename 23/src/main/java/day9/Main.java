package day9;

public class Main {
    
    public static void main(String[] args) {
        String input = InputReader.getInput("input.txt");
        Snake snake = new Snake();

        for (String line : input.split("\n")){
            char direction = line.split(" ")[0].charAt(0);
            int number = Integer.parseInt(line.split(" ")[1]);

            snake.moveHead(direction, number);
        }

        System.out.println(snake.getVisitedPositions().size());
    }
}
