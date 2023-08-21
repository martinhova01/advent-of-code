package day9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SnakeP1 {
    
    private Position head;
    private Position tail;
    private Position startPos;
    private List<Position> visitedPositions = new ArrayList<>();

    private static final Integer[] UP = {0, 1};
    private static final Integer[] DOWN = {0, -1};
    private static final Integer[] RIGHT = {1, 0};
    private static final Integer[] LEFT = {-1, 0};
    private static final Integer[] UP_LEFT = {-1, 1};
    private static final Integer[] UP_RIGHT = {1, 1};
    private static final Integer[] DOWN_LEFT = {-1, -1};
    private static final Integer[] DOWN_RIGHT = {1, -1};
    private static final Integer[][] DIAGONAL_DIRECTIONS = {UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT};
    private final Map<Character, Integer[]> directions = new HashMap<>(Map.of('U', UP, 'D', DOWN, 'R', RIGHT, 'L', LEFT));

    public SnakeP1(){
        head = new Position(0, 0);
        tail = new Position(0, 0);
        startPos = new Position(0, 0);
        visitedPositions.add(startPos);
    }

    public void moveHead(char direction, int number){
        int x = directions.get(direction)[0];
        int y = directions.get(direction)[1];

        
        for(int i = 0; i < number; i++){
            head.setX(head.getX() + x);
            head.setY(head.getY() + y);

            if (isTwoStepsApart()){
                moveTail(directions.get(direction));
            }

            else if(!head.isTouching(tail) && (tail.getX() != head.getX() && tail.getY() != head.getY())){
                moveTail(correctDiogonalDirection());
            }

        }
    }

    private Integer[] correctDiogonalDirection() {
        

        for (Integer[] direction : DIAGONAL_DIRECTIONS){
            Position tempPos = new Position(tail.getX(), tail.getY());
            tempPos.setX(tempPos.getX() + direction[0]);
            tempPos.setY(tempPos.getY() + direction[1]);

            if (tempPos.isTouching(head)){
                return direction;
            }
        }
        return null;

    }
    private boolean isTwoStepsApart() {

        for(Integer[] direction : directions.values()){
            int x = direction[0] * 2;
            int y = direction[1] * 2;

            Position tempPos = new Position(head.getX() + x, head.getY() + y);
            if (tempPos.equals(tail)){
                return true;
            }
        }
        return false;
    }
    public void moveTail(Integer[] direction){
        int x = direction[0];
        int y = direction[1];

        tail.setX(tail.getX() + x);
        tail.setY(tail.getY() + y);

        boolean contains = false;
        for (Position position : visitedPositions) {
            if(position.equals(tail)){
                contains = true;
                break;
            }
        }
        if (!contains){
            visitedPositions.add(new Position(tail.getX(), tail.getY()));
        }
    }

    public Position getTail(){
        return tail;
    }

    public List<Position> getVisitedPositions(){
        return visitedPositions;
    }

    public static void main(String[] args) {
        SnakeP1 snake = new SnakeP1();

        snake.moveHead('U', 1);
        snake.moveHead('R', 2);

        System.out.println(snake.head.getX() + " " + snake.head.getY());
        System.out.println(snake.tail.getX() + " " + snake.tail.getY() );

    }
}
