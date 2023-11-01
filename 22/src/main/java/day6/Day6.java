package day6;
import java.util.ArrayList;
import java.util.List;
import util.InputReader;

public class Day6 {
    

    public static void main(String[] args) {
        String input = InputReader.getInput("../day6/day6.txt");

        int marker = 0;
        int index = 13;
        List<Character> characters = new ArrayList<>();
        for(int i = 0; i < 14; i++){
            characters.add(input.charAt(i));
        }
        
        while(marker == 0){
            long distinctCharacters = characters.stream().distinct().count();
            if (distinctCharacters == 14){
                marker = index;
            }
            else{
                index++;
                characters.remove(0);
                characters.add(input.charAt(index));
            }
            
        }

        System.out.println(marker + 1);
    }
}
