package day17;

import java.util.ArrayList;
import java.util.List;

public class I extends Rock{
    
    public I() {
        shape = new ArrayList<>();
        shape.add(new ArrayList<>(List.of('@', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('@', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('@', '.', '.', '.')));
        shape.add(new ArrayList<>(List.of('@', '.', '.', '.')));
    }

    @Override
    protected void setWidthAndHeight() {
        this.width = 1;
        this.height = 4;
    }
}
