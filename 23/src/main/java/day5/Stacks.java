package day5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class Stacks {
    private List<Stack<Character>> stacks;

    public Stacks(){
        stacks = new ArrayList<Stack<Character>>();
        for(int i = 1; i <= 9; i++){
            stacks.add(new Stack<>());
        }
    }

    public Character pop(int index){
        return stacks.get(index).pop();
    }

    public List<Character> popMultiple(int index, int numberofElements){
        List<Character> result = new ArrayList<>();
        for (int i = 0; i < numberofElements; i++){
            result.add(this.pop(index));
        }
            //reverse list
        Collections.reverse(result);
        return result;
    }
    public void push(int index, Character c){
        this.stacks.get(index).push(c);
    }

    public void pushMultiple(int stackIndex, List<Character> elements){
        for (Character c : elements) {
            this.push(stackIndex, c);
        }
    }

    public Stack<Character> getStack(int index){
        return stacks.get(index);
    }

    public Character peek(int stack, int index){
        return this.getStack(stack).lastElement();
    }
}
