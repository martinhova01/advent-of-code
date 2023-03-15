package day10;

public class CycleListener {

    private int signalStrength;
    private String drawing = "";
    
    public void update(int cycle, int value){
        if(cycle % 40 == 20){
            signalStrength += cycle * value;
        }
    }

    public void draw(int cycle, int value){
        cycle = cycle % 40;
        if (cycle % 40 == 0){
            drawing += "\n";
        }
        if (value -1 == cycle || value == cycle || value +1 == cycle){
            drawing += "#";
        }
        else{
            drawing += ".";
        }
    }

    public int getSignalStrength() {
        return signalStrength;
    }

    public String getDrawing(){
        return drawing;
    }
}
