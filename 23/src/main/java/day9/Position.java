package day9;

public class Position {
    
    private int x;
    private int y;

    public Position(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }
    
    public boolean equals(Position otherPos){
        if (this.getX() == otherPos.getX() && this.getY() == otherPos.getY()){
            return true;
        }
        return false;
    }

    public boolean isTouching(Position otherPos){
        
        for (int x = -1; x <= 1; x++ ){
            for(int y = -1; y <= 1; y++){
                Position tempPos = new Position(this.getX() + x, this.getY() + y);
                if (tempPos.equals(otherPos)){
                    return true;
                }
            }
        }
        return false;
    }
}
