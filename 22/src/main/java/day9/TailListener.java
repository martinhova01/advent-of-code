package day9;

import java.util.ArrayList;
import java.util.List;

public class TailListener {

    List<Position> visitedPositions = new ArrayList<>();

    public void addVisitedPos(Position pos){
        if (!hasVisited(pos)){
            visitedPositions.add(pos);
        }
    }
    private boolean hasVisited(Position pos){
        for (Position p : visitedPositions){
            if (p.getX() == pos.getX() && p.getY() == pos.getY()){
                return true;
            }
        }
        return false;
    }

    public int getNumberOfVisitedPositions(){
        return visitedPositions.size();
    }
    public void printVisitedPos() {
        for(Position p : visitedPositions){
            System.out.println("(" + p.getX() + ", " + p.getY() + ")");
        }
    }
    
}
