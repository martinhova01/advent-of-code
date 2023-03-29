package day12;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

public class BFS {

    private int rows;
    private int cols;
    private List<List<Character>> heightMap;
    private int startRow;
    private int startCol = 0;
    private Queue<Integer> qRow = new ArrayDeque<>();
    private Queue<Integer> qCol = new ArrayDeque<>();

    private int moveCount = 0;
    private int nodesLeftInLayer = 1;
    private int nodesInNextLayer = 0;

    private boolean reachedEnd = false;

    private List<List<Boolean>> visited;

    private static final int[] dRow = {-1, 1, 0, 0};
    private static final int[] dCol = {0, 0, 1, -1};


    public BFS(int rows, int cols, List<List<Character>> heightMap, int startRow, int startCol) {
        this.rows = rows;
        this.cols = cols;
        this.heightMap = heightMap;
        this.startRow = startRow;
        this.startCol = startCol;

        this.visited = new ArrayList<>();
        for(int i = 0; i < rows; i ++){
            List<Boolean> newRow = new ArrayList<>();
            for (int j = 0; j < cols; j++){
                newRow.add(false);
            }
            visited.add(newRow);
        }
    }

    public int solve(){
        qRow.add(startRow);
        qCol.add(startCol);
        visited.get(startRow).set(startCol, true);

        while(qRow.size() > 0){
            int r = qRow.poll();
            int c = qCol.poll();

            if(heightMap.get(r).get(c) == 'E'){
                reachedEnd = true;
                break;
            }
            exploreNeighbours(r, c);
            nodesLeftInLayer--;
            if(nodesLeftInLayer == 0){
                nodesLeftInLayer = nodesInNextLayer;
                nodesInNextLayer = 0;
                moveCount++;
            }
        }
        if(reachedEnd){
            return moveCount;
        }
        return -1;
    }

    private void exploreNeighbours(int r, int c) {
        char height = heightMap.get(r).get(c);
        if (height == 'S'){
            height = 'a';
        }
        for (int i = 0; i < 4; i++){
            int nextR = r + dRow[i];
            int nextC = c + dCol[i];
            
            //out of bounds
            if(nextR < 0 || nextC < 0 || nextR >= rows || nextC >= cols){
                continue;
            }
            //node already visited
            if(visited.get(nextR).get(nextC)){
                continue;
            }
            char nextHeight = heightMap.get(nextR).get(nextC);
            if (nextHeight == 'E'){
                nextHeight = 'z';
            }
                //next node is too high
            if (nextHeight - height > 1){
                continue;
            }

            qRow.add(nextR);
            qCol.add(nextC);
            visited.get(nextR).set(nextC, true);
            nodesInNextLayer++;
        }
    }
}

