package day17;

import java.util.List;

public  abstract class Rock {

        // '.' = empty space and '@' = rock
    protected List<List<Character>> shape;

    protected int width;
    protected int height;


    public Rock(){
        setWidthAndHeight();
    }

    public List<List<Character>> getShape(){
        return this.shape;
    }

    protected abstract void setWidthAndHeight();

    public int getWidth(){
        return width;
    }

    public int getHeight(){
        return height;
    }

}
