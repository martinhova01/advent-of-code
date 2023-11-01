package day3;
import java.util.HashSet;
import java.util.Set;

import util.InputReader;

public class Day3 {
    
    private static String priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static int findCommonItemPriority(String rucksack){
        String compartment1 = rucksack.substring(0, rucksack.length() / 2);
        String compartment2 = rucksack.substring(rucksack.length() / 2);

            //find common item
        char commonItem = '0';
        for(int i = 0; i < compartment1.length(); i++){
            char item1 = compartment1.charAt(i);
            for (int j = 0; j < compartment2.length(); j++){
                char item2 = compartment2.charAt(j);
                if (item1 == item2){
                    commonItem = item1;
                }
            }
        }

        return priorities.indexOf(commonItem);
    }

    public static int findCommonItemPriority(String rucksack1, String rucksack2, String rucksack3) {
        Set<Character> elf1 = new HashSet<>();
        Set<Character> elf2 = new HashSet<>();
        Set<Character> elf3 = new HashSet<>();

        addElementsToSet(elf1, rucksack1);
        addElementsToSet(elf2, rucksack2);
        addElementsToSet(elf3, rucksack3);

        Set<Character> intersection = new HashSet<>(elf1);
        intersection.retainAll(elf2);
        intersection.retainAll(elf3);

        char commonItem = intersection.stream().findFirst().get();

        return priorities.indexOf(commonItem);
        
        

    }

    private static void addElementsToSet(Set<Character> set, String s){
        for(int i = 0; i < s.length(); i++){
            set.add(s.charAt(i));
        }
    }


    public static void main(String[] args) {
        String input = InputReader.getInput("../day3/day3.txt");
        String[] rucksacks = input.split("\n");

            //Part 1
        int sum1 = 0;
        for (String rucksack : rucksacks) {
            sum1 += findCommonItemPriority(rucksack);
        }
        System.out.println(sum1);


            //Part 2
        int sum2 = 0;
            for(int i = 3; i <= rucksacks.length; i += 3){
                sum2 += findCommonItemPriority(rucksacks[i-3], rucksacks[i-2], rucksacks[i-1]);
            }
            System.out.println(sum2);
        
        
    }


    
}
