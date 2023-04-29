package day17;

import java.util.ArrayList;
import java.util.List;

public class Square extends Rock{
    
    public Square() {
        shape = new ArrayList<>();
        shape.add(new ArrayList<>(List.of('@', '@', '.', '.')));
        shape.add(new ArrayList<>(List.of('@', '@', '.', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
    }

    @Override
    protected void setWidthAndHeight() {
        this.width = 2;
        this.height = 2;
    }
}
