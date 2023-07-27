package day14;

import java.util.ArrayList;
import java.util.List;

public class Grid {

    List<List<Character>> grid;
    int sandX = 300;
    int sandY = 0;
    boolean finished;

    public Grid(int rows, int cols){
        grid = new ArrayList<>();

        for(int i = 0; i < rows; i++){
            List<Character> newRow = new ArrayList<>();

            for (int j = 0; j < cols; j++){
                newRow.add('.');
            }
            grid.add(newRow);
        }
        
    }

    public void print(){
        String result = "";
        for (List<Character> row : grid) {
            for (char c : row) {
                result += c;
            }
            result+= "\n";
        }
        System.out.println(result);
    }

    public void replace(int x, int y, char c){
        grid.get(y).set(x, c);
    }

    public void spawnSand(){
        replace(300, 0, 'o');
        if(get(299, 1) == 'o' && get(300, 1) == 'o' && get(301, 1) == 'o'){
            finished = true;
        }
        sandX = 300;
        sandY = 0;
    }
    public char get(int x, int y){
        return grid.get(y).get(x);
    }

    public boolean moveSand(){
        if(sandY == 199){
            replace(sandX, sandY, '.');
            finished = true;
            return true;
        }
        else if (get(sandX, sandY + 1) == '.'){
            replace(sandX, sandY, '.');
            sandY++;
            replace(sandX, sandY, 'o');
            return true;
        }
        else if(get(sandX - 1, sandY + 1) == '.'){
            replace(sandX, sandY, '.');
            sandX--;
            sandY++;
            replace(sandX, sandY, 'o');
            return true;
        }
        else if(get(sandX + 1, sandY + 1) == '.'){
            replace(sandX, sandY, '.');
            sandX++;
            sandY++;
            replace(sandX, sandY, 'o');
            return true;
        }
        else{
            return false;
        }
    }

    public int countSand(){
        int count = 0;
        for (List<Character> row : grid) {
            for (Character c : row) {
                if (c == 'o'){
                    count++;
                }
            }
        }
        return count;
    }

    public boolean isFinished(){
        return finished;
    }

    public static void main(String[] args) {
        Character c = '.';
        System.out.println(c == '.');
    }
    
}
