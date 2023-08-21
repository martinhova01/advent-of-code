package day9;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SnakeP2 {

    private int length;
    private List<Position> body;
    private TailListener listener;
    

    private static final Direction UP = new Direction(0, 1);
    private static final Direction DOWN = new Direction(0, -1);
    private static final Direction RIGHT = new Direction(1, 0);
    private static final Direction LEFT = new Direction(-1, 0);
    private static final Direction UP_LEFT = new Direction(-1, 1);
    private static final Direction UP_RIGHT = new Direction(1, 1);
    private static final Direction DOWN_LEFT = new Direction(-1, -1);
    private static final Direction DOWN_RIGHT = new Direction(1, -1);


    private static final Collection<Direction> DIAGONAL_DIRECTIONS = List.of(UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT);
    private final Map<Character, Direction> STRAIGHT_DIRECTIONS = new HashMap<>(Map.of('U', UP, 'D', DOWN, 'R', RIGHT, 'L', LEFT));

    public SnakeP2(){
        length = 10;
        body = new ArrayList<>();
        for (int i = 0; i < length; i++){
            body.add(new Position(0, 0));
        }
        listener = new TailListener();
        body.get(length - 1).setListner(listener);
        listener.addVisitedPos(new Position(0, 0));
    }

    public void moveHead(char direction){
        int x = STRAIGHT_DIRECTIONS.get(direction).getX();
        int y = STRAIGHT_DIRECTIONS.get(direction).getY();

        Position head = this.body.get(0);
        head.setX(head.getX() + x);
        head.setY(head.getY() + y);
        
        for(int i = 1; i < body.size(); i++){
            Position p1 = body.get(i - 1);
            Position p2 = body.get(i);

            if (isTwoStepsApart(p1, p2)){
                p2.moveDirection(STRAIGHT_DIRECTIONS.get(direction));
            }

            else if(!p1.isTouching(p2) && (p2.getX() != p1.getX() && p2.getY() != p1.getY())){
                p2.moveDirection(correctDiogonalDirection(p1, p2));
            }

        }
    }

    private Direction correctDiogonalDirection(Position head, Position tail) {
        

        for (Direction dir : DIAGONAL_DIRECTIONS){
            Position tempPos = new Position(tail.getX(), tail.getY());
            tempPos.setX(tempPos.getX() + dir.getX());
            tempPos.setY(tempPos.getY() + dir.getY());

            if (tempPos.isTouching(head)){
                return dir;
            }
        }
        return null;

    }
    private boolean isTwoStepsApart(Position p1, Position p2) {

        for(Direction dir : STRAIGHT_DIRECTIONS.values()){
            int xOffset = dir.getX() * 2;
            int yOffset = dir.getY() * 2;

            Position tempPos = new Position(p1.getX() + xOffset, p1.getY() + yOffset);
            if (tempPos.equals(p2)){
                return true;
            }
        }
        return false;
    }

    public int getNumberOfVisitedPositions(){
        return listener.getNumberOfVisitedPositions();
    }

    public void printVisitedPos(){
        listener.printVisitedPos();
    }
}
