package day13;

import java.util.ArrayList;
import java.util.List;

public class Packet implements Comparable<Packet> {

    private List<String> data = new ArrayList<>();

    public Packet(String input){
        String  strippedInput = input.substring(1, input.length() - 1);
        
        for(String element : input.substring(1, input.length() - 1).split(",")){
            data.add(element);
        }
    }


    @Override
    public int compareTo(Packet p) {
        for(int i = 0; i < data.size(); i++){
            String elementThis = this.data.get(i);
            String elementP = "";

            try{
                elementP = p.data.get(i);
            }
            catch(IndexOutOfBoundsException e){
                return 1;
            }

                //both are numbers
            if (isNumeric(elementThis) && isNumeric(elementP)){
                if(Integer.parseInt(elementThis) - Integer.parseInt(elementP) == 0){
                    continue;
                }
                return Integer.parseInt(elementThis) - Integer.parseInt(elementP);
            }
                //both are lists
            else if (isList(elementThis) && isList(elementP)){
                return new Packet(elementThis).compareTo(new Packet(elementP));
            }

                //exactly one is an integer
            else {
                    //convert elementThis to list
                if (isNumeric(elementThis)){
                    return new Packet("[" + elementThis + "]").compareTo(new Packet(elementP));
                }
                    //convert elementP to list
                else{
                    return new Packet(elementThis).compareTo(new Packet("[" + elementP + "]"));
                }
            }
        }
        return 0;
    }
    
    @Override
    public String toString() {
        return data.toString();
    }

        //From https://stackoverflow.com/questions/1102891/how-to-check-if-a-string-is-numeric-in-java
    private boolean isNumeric(String str) {
        return str.matches("-?\\d+(\\.\\d+)?");
    }

    private boolean isList(String str){
        return str.startsWith("[") && str.endsWith("]");
    }
    

    public static void main(String[] args) {
        Packet p = new Packet("[[8,7,6]]");
        System.out.println(p);
    }
    
}
