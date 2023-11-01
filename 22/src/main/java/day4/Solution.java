package day4;

import java.util.Arrays;
import java.util.List;
import util.InputReader;

public class Solution {
    
    public static void main(String[] args) {
        String input = InputReader.getInput("../day4/day4.txt");
        String[] pairs = input.split("\n");

        int containsCounter = 0;
        int overlapCounter = 0;
        for(String pair: pairs){
            String range1 = pair.split(",")[0]; //example: "1-7"
            String range2 = pair.split(",")[1];

            List<Integer> sections1 = Arrays.stream(range1.split("-"))
            .map(a -> Integer.parseInt(a))
            .toList();
            List<Integer> sections2 = Arrays.stream(range2.split("-"))
            .map(a -> Integer.parseInt(a))
            .toList();

            SectionSpan elf1 = new SectionSpan(sections1.get(0), sections1.get(1));
            SectionSpan elf2 = new SectionSpan(sections2.get(0), sections2.get(1));

            if (elf1.contains(elf2) || elf2.contains(elf1)){
                containsCounter++;
                overlapCounter++;
            }
            else if (elf1.overlaps(elf2)){
                overlapCounter++;
            }
        }

        System.out.println(containsCounter);
        System.out.println(overlapCounter);
    }
}
