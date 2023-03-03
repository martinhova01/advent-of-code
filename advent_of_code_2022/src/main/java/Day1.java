
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class Day1{

    public static int d1p1(String input){
        int largest = 0;
        int sum = 0;

        List<String> lines = input.lines().toList();

        for (String line : lines) {
            if (line.length() > 0){
                sum += Integer.parseInt(line);
            }
            else{
                if (sum > largest){
                    largest = sum;
                }
                sum = 0;
            }
        }

        return largest;

    }

    public static int d1p2(String input){

        List<String> lines = input.lines().toList();

        List<Integer> sums = new ArrayList<>();
        int sum = 0;
        for (String line : lines) {
            if (line.length() > 0){
                sum += Integer.parseInt(line);
            }
            else{
                sums.add(sum);
                sum = 0;
            }
        }
        Collections.sort(sums, (a, b) -> b - a);
        int result = 0;
        for (int i = 0; i < 3; i++){
            result += sums.get(i);
        }

        return result;


    }
    
    public static void main(String[] args) {
        String input = InputReader.getInput("puzzleInputs/day1.txt");
        System.out.println(d1p1(input));
        System.out.println(d1p2(input));
    }
}