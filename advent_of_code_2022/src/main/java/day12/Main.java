package day12;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String input = InputReader.getInput("input.txt");
        int rows = input.split("\n").length;
        int cols = -1;

        List<List<Character>> heightMap = new ArrayList<>();
        int startRow = -1;
        int startCol = 0;

            //add the input characters to the heightmap
        for(int i = 0; i < rows; i++){
            String line = input.split("\n")[i];
            cols = line.length();
            if (line.startsWith("S")){
                startRow = i;
            }
            List<Character> newRow = new ArrayList<>();

            for (int j = 0; j < cols; j ++){
                char c = line.charAt(j);
                newRow.add(c);
            }
            heightMap.add(newRow);
        }

            //part 1
        int part1 = new BFS(rows, cols, heightMap, startRow, startCol).solve();
        System.out.println("Part 1: " + part1);

            //part 2
        int shortest = part1;
        for (int i = 0; i < heightMap.size(); i++) {
            List<Character> row = heightMap.get(i);
            for (int j = 0; j < cols; j++) {
                if(row.get(j).equals('a')){
                    int path = new BFS(rows, cols, heightMap, i, j).solve();
                    if(path < shortest && path != -1){
                        shortest = path;
                    }
                }
                
            }
            
        }

        System.out.println("Part 2: " + shortest);
    }
    
}
