package day2;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Day2 {
    public static final Map<String, Integer> shapeScores1 = Map.of("X", 1, "Y", 2, "Z", 3);
    public static final Map<String, Integer> shapeScores2 = Map.of("A", 1, "B", 2, "C", 3);
    public static final List<String> shapes = List.of("A", "B", "C");

    public static int calculateScore(String opponent, String you){
        int shapeScore = shapeScores1.get(you);
        int outcomeScore = 0;
            //draw
        if (roundResult(opponent, you) == 0){
            outcomeScore = 3;
        }
            // win
        else if(roundResult(opponent, you) == 1){
            outcomeScore = 6;
        }
            //Lost
        else{
            outcomeScore = 0;
        }

        return outcomeScore + shapeScore;
    }

    private static boolean isEqual(String you, String opponent){
        if ((you.equals("X") && opponent.equals("A")) ||
            (you.equals("Y") && opponent.equals("B")) || 
            (you.equals("Z") && opponent.equals("C"))){
            return true;
        }
        return false;
    }
        //return -1 for loss, 0 for draw and 1 for win
    private static int roundResult(String opponent, String you){
        //draw
        if (isEqual(you, opponent)){
            return 0;
        }
            // win
        else if((opponent.equals("A") && you.equals("Y")) ||
                (opponent.equals("B") && you.equals("Z")) ||
                (opponent.equals("C") && you.equals("X"))){
            return 1;
        }
            //Lost
        else{
            return -1;
        }
    }

    public static int calculateScore2(String opponent, String result){
        int outcomeScore;
        int shapeScore;
            //Loss
        if (result.equals("X")){
            outcomeScore = 0;

            int index = shapes.indexOf(opponent) - 1;
            if (index == -1){index = 2;}
            String shape = shapes.get(index);
            
            shapeScore = shapeScores2.get(shape);
        }
            //Draw
        else if (result.equals("Y")){
            outcomeScore = 3;
            String shape = opponent;
            shapeScore = shapeScores2.get(shape);
        }
            //win
        else{
            outcomeScore = 6;

            int index = shapes.indexOf(opponent)+1;
            if (index == 3){index = 0;}
            String shape = shapes.get(index);
            shapeScore = shapeScores2.get(shape);
        }
            

        return outcomeScore + shapeScore;
    }

    public static void main(String[] args) {
        String input = InputReader.getInput("day2.txt");
        List<List<String>> rounds = input.lines().map(line -> Arrays.stream(line.split(" ")).toList()).toList();
        

        int totalScore1 = 0;
        int totalScore2 = 0;
        for (List<String> round : rounds) {
            totalScore1 += calculateScore(round.get(0), round.get(1));
            totalScore2 += calculateScore2(round.get(0), round.get(1));
        }
            //Answers to part 1 and 2
        System.out.println(totalScore1);
        System.out.println(totalScore2);
    }
}
