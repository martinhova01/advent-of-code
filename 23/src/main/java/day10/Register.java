package day10;

public class Register {
    
    private int cycle;
    private int value;
    private CycleListener listener;

    public Register(){
        this.cycle = 0;
        this.value = 1;
        this.listener = new CycleListener();
    }

    public void noop(){
        listener.draw(cycle, value);
        cycle++;
        listener.update(cycle, value);
    }

    public void add(int value){
        noop();
        noop();
        this.value += value;
    }

    public CycleListener getlistener(){
        return listener;
    }

    public int getCycle() {
        return cycle;
    }

    public int getValue() {
        return value;
    }

    
}
