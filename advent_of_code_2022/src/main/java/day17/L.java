package day17;

import java.util.ArrayList;
import java.util.List;

public class L extends Rock{
    
    public L() {
        shape = new ArrayList<>();
        shape.add(new ArrayList<>(List.of('@', '@', '@', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '@', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '@', '.')));
        shape.add(new ArrayList<>(List.of('.', '.', '.', '.')));
    }

    @Override
    protected void setWidthAndHeight() {
        this.width = 3;
        this.height = 3;
    }

}
