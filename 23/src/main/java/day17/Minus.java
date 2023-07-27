package day17;

import java.util.ArrayList;
import java.util.List;

public class Minus extends Rock{

    public Minus() {
        shape = new ArrayList<>();
        shape.add(new ArrayList<>(List.of('@', '@', '@', '@')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
    }

    @Override
    protected void setWidthAndHeight() {
        this.width = 4;
        this.height = 1;
    }
    
}
