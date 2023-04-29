package day17;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Chamber {

    private int width;
    private List<List<Character>> grid;
    private int currentRow;
    private int currentCol;
    private Rock currentRock;

    public Chamber(int width){
        this.width = width;
        this.currentRow = 0;
        this.currentCol = 2;
        grid = new ArrayList<>();

        for(int i = 0; i < 1000000; i++){
            List<Character> newRow = new ArrayList<>();
            for(int j = 0; j < width; j++){
                newRow.add('.');
            }
            grid.add(newRow);
        }
    }

    public void spawnRock(Rock r){
        currentRock = r;

            //find the row to spawn the rock
        currentCol = 2;
        while(true){
            if(isEmptyRow(grid.get(currentRow))){
                currentRow += 3;
                break;
            }
            currentRow++;
        }

        drawRock(currentRow, currentCol, '@');

    }

    public boolean moveRockDown(){
        if(isStopped()){
            drawRock(currentRow, currentCol, '#');
            return false;
        }
        removeActiveRock();
        currentRow--;
        drawRock(currentRow, currentCol, '@');
        return true;
    }

    private boolean isStopped() {
        if(currentRow == 0){
            return true;
        }
        for(int i = currentCol; i < currentCol + currentRock.getWidth(); i++){

            int counter = 0;
            while(grid.get(currentRow + counter).get(i) != '@'){
                counter++;
            }

            if (grid.get(currentRow + counter - 1).get(i) == '#'){
                return true;
            }
        }
        return false;
    }

    public void moveRockLeft(){
            //rock hit another rock  or wall to the left
        if (isHitLeft()){
            return;
        }

        removeActiveRock();
        currentCol--;
        drawRock(currentRow, currentCol, '@');
    }

    private boolean isHitLeft() {
        if(currentCol - 1 < 0){
            return true;
        }
        for(int i = currentRow; i < currentRow + currentRock.getHeight(); i++){
            int counter = 0;
            while(grid.get(i).get(currentCol + counter) != '@'){
                counter++;
            }

            if (grid.get(i).get(currentCol + counter - 1) == '#'){
                return true;
            }
        }
        return false;
    }

    public void moveRockRight(){
            //rock hit another rock or wall to the right
        if (isHitRight()){
            return;
        }
        removeActiveRock();
        currentCol++;
        drawRock(currentRow, currentCol, '@');
    }

    private boolean isHitRight() {
        if(currentCol + currentRock.getWidth() + 1 > width){
            return true;
        }
        for(int i = currentRow; i < currentRow + currentRock.getHeight(); i++){


            int counter = 1;
            while(grid.get(i).get(currentCol + currentRock.getWidth() - counter) != '@'){
                counter++;
            }


            if (grid.get(i).get(currentCol + currentRock.getWidth() - counter + 1) == '#'){
                return true;
            }
        }
        return false;
    }

    private void removeActiveRock() {
        for(int i = currentRow; i < currentRow + currentRock.getHeight(); i++){
            for(int j = currentCol; j < currentCol + currentRock.getWidth(); j++){

                if (currentRock.getShape().get(i - currentRow).get(j - currentCol) == '@'){
                    grid.get(i).set(j, '.');
                }
            }
        }
    }

    private void drawRock(int row, int col, char c){
        for(int i = row; i < row + currentRock.getHeight(); i++){
            for (int j = col; j < col + currentRock.getWidth(); j++){
                if (currentRock.getShape().get(i - row).get(j - col) == '@'){
                    grid.get(i).set(j, c);
                }

            }
        }
    }

    private boolean isEmptyRow(List<Character> row){
        for (Character c : row) {
            if (c != '.'){
                return false;
            }
        }
        return true;
    }

    public String print(int rows){
        String result = "";
        for (int i = rows; i >= 0; i--) {
            for(int j = 0; j < width; j++){
                result += grid.get(i).get(j);
            }
            result += "\n";
            
        }
        return result;
    }

    public void write(int rows) {
        try (FileWriter fileWriter = new FileWriter("C:/Users/marti/Desktop/advent-of-code-2022/advent_of_code_2022/src/main/java/day17/write.txt")) {
            String data = print(rows);
            
            fileWriter.write(data);
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int getHeight(){
        int i = 0;
        while (!isEmptyRow(grid.get(i))){
            i++;
        }
        return i;
    }
    
}
