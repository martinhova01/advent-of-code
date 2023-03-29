package day11;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;

public class Monkey {
    
    private int number;
    private List<Integer> items;
    private UnaryOperator<Long> operation;
    private Predicate<Integer> test;
    private Monkey nextTrue;
    private Monkey nextFalse;
    private int inspections = 0;

    public Monkey(int number, UnaryOperator<Long> operation, Predicate<Integer> test, int...items) {
        this.number = number;
        this.items = new ArrayList<>();
        Arrays.stream(items).forEach(i -> this.items.add(i));
        this.operation = operation;
        this.test = test;
    }

    public void addItem(Integer i){
        items.add(i);
    }
    

    public void setNextTrue(Monkey nextTrue) {
        this.nextTrue = nextTrue;
    }

    public void setNextFalse(Monkey nextFalse) {
        this.nextFalse = nextFalse;
    }

    @Override
    public String toString() {
        return "Monkey [number=" + number + ", items=" + items
                + "]";
    }


    public int getInspections() {
        return inspections;
    }

        //part 1
    public void turn(){
        for (Integer item : items) {
            inspections++;
            item = (int)(long)operation.apply((long)item);
            item = item / 3;
            if (test.test(item)){
                nextTrue.addItem(item);
            }
            else{
                nextFalse.addItem(item);
            }
        }
        items.clear();
    }
        //part 2
    public void turn2(){
        for (Integer item : items) {
            inspections++;
            long temp = operation.apply((long)item);
            temp = temp % 9699690;  
            item = (int) temp;
            
            if (test.test(item)){
                nextTrue.addItem(item);
            }
            else{
                nextFalse.addItem(item);
            }
        }
        items.clear();
    }
    
}
