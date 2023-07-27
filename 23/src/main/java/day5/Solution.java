package day5;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    public static ArrayList<Character> splitLine(String line){

        ArrayList<Character> result = new ArrayList<>();
        for (int i = 1; i < line.length(); i += 4){
            
            result.add(line.charAt(i));
        }
        return result;
    }
    

    public static void main(String[] args) {
        Stacks stacks = new Stacks();
        String input = InputReader.getInput("day5.txt");

        String setup = input.split("\n\n")[0];
        String procedure = input.split("\n\n")[1];

        String[] setupLines = setup.split("\n");

        for (int i = setupLines.length - 2; i >= 0; i--){
            List<Character> crates = splitLine(setupLines[i]);
            for (int j = 0; j < crates.size(); j++) {
                stacks.push(j, crates.get(j));
            }
        }

            //remove empty spaces in stacks
        for (int i = 0; i < 9; i++){
            Stack<Character> stack = stacks.getStack(i);
            while(stack.peek() == ' '){
                stack.pop();
            }
        }

            //Perform procedure
        String[] procedureLines = procedure.split("\n");

        for (String line : procedureLines){
            String[] words = line.split(" ");
            int numberOfCrates = Integer.parseInt(words[1]);
            int fromStack = Integer.parseInt(words[3]) - 1;
            int toStack = Integer.parseInt(words[5]) - 1;

                //part 1
            // for(int i = 0; i < numberOfCrates; i++){
            //     stacks.push(toStack, stacks.pop(fromStack));
            // }

                //part 2
            stacks.pushMultiple(toStack, stacks.popMultiple(fromStack, numberOfCrates));
            for (int i = 0; i < 9; i++){
                System.out.println(stacks.getStack(i));
            }
            System.out.println();
        }

        String result = "";
        for(int i = 0; i < 9; i++){
            result += "" + stacks.pop(i);
        }

        System.out.println(result);


    }
}
