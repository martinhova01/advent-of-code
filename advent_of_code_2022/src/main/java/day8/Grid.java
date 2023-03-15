package day8;

import java.util.ArrayList;
import java.util.List;

public class Grid {
    
    private List<List<Integer>> grid;

    public Grid(){
        grid = new ArrayList<>();
    }

    public void addRow(List<Integer> row){
        grid.add(row);
    }

    public int get(int row, int colum){
        if (row == -1 || colum == -1 || row >= grid.size() || colum >= grid.get(0).size()){
            return -1;
        }
        return grid.get(row).get(colum);
    }

    public List<List<Integer>> getGrid(){
        return grid;
    }

    public boolean isVisible(int row, int colum) {

        int height = get(row, colum);
        int r, c;
        List<List<Integer>> directions = List.of(List.of(0, 1), List.of(0, -1), List.of(1, 0), List.of(-1, 0));
        for(List<Integer> direction : directions){
            r = direction.get(0);
            c = direction.get(1);

            int j = 1;
            while(true){
                int treeHeight = get(row + r*j, colum + c*j);
                if (treeHeight == -1){
                    return true;
                }
                else if(treeHeight >= height){
                    break;
                }
                j++;
            }
        }
        return false;
    }

    public int getScenicScore(int row, int colum) {

        int height = get(row, colum);
        int r, c;
        List<Integer> viewingDistances = new ArrayList<>();
        List<List<Integer>> directions = List.of(List.of(0, 1), List.of(0, -1), List.of(1, 0), List.of(-1, 0));
        for(List<Integer> direction : directions){
            r = direction.get(0);
            c = direction.get(1);

            int j = 1;
            while (true){
                int treeHeight =get(row + r*j, colum + c*j);
                if (treeHeight == -1){
                    j--;
                    break;
                }
                else if( treeHeight >= height){
                    break;
                }
                j++;
            }
            viewingDistances.add(j);
        }

        int scenincScore = 1;
        for (Integer dist : viewingDistances) {
            scenincScore *= dist;
        }
        return scenincScore;
    }
}
