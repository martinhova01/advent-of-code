package day17;

import java.util.List;

import util.InputReader;

public class Main {
    
    public static void main(String[] args) {
        List<Rock> rocks = List.of(new Minus(), new Pluss(), new L(), new I(), new Square());
        int width = 7;
        String input = InputReader.getInput("../day17/input.txt");
        input = input.strip();

        
        int rocksCounter = 0;
        int inputCounter = 0;
        int rocksSpawned = 1;
        
        Chamber c = new Chamber(width);
        c.spawnRock(rocks.get(rocksCounter));
        rocksCounter++;
        while(rocksSpawned < 2023){

                //wind
            if(input.charAt(inputCounter) == '>'){
                c.moveRockRight();
            }
            else {
                c.moveRockLeft();
            }
            inputCounter++;
            inputCounter = inputCounter % input.length();

                //gravity
            if(!c.moveRockDown()){
                c.spawnRock(rocks.get(rocksCounter));
                rocksSpawned++;

                rocksCounter++;
                rocksCounter = rocksCounter % 5;

            }
        }
        System.out.println("Part 1: " + c.getHeight());
        // c.write(3200);


    }
}
