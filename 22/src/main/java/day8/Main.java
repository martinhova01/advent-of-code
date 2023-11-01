package day8;

import java.util.ArrayList;
import java.util.List;
import util.InputReader;


public class Main {
    
    public static void main(String[] args) {
        String input = InputReader.getInput("../day8/input.txt");
        Grid grid = new Grid();

        for(String line : input.split("\n")){
            List<Integer> newRow = new ArrayList<>();
            for(int i = 0; i < line.length(); i++){
                newRow.add(Integer.parseInt(line.substring(i, i + 1)));
            }
            grid.addRow(newRow);
        }

        int visibleTrees = 0;
        for (int i = 0; i < grid.getGrid().size(); i++) {
            for (int j = 0; j < grid.getGrid().get(0).size(); j++) {
                if(grid.isVisible(i, j)){
                    visibleTrees++;
                }
            }
        }
            //solution part 1
        System.out.println("Part 1: " + visibleTrees);


        int largetsScenicScore = 0;
        for (int i = 0; i < grid.getGrid().size(); i++) {
            for (int j = 0; j < grid.getGrid().get(0).size(); j++) {
                int scenicScore = grid.getScenicScore(i, j);
                if (scenicScore > largetsScenicScore){
                    largetsScenicScore = scenicScore;
                }
            }
        }
            //solution part 2
        System.out.println("Part 2: " + largetsScenicScore);

    }
}
