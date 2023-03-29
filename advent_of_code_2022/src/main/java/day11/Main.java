package day11;

import java.util.List;

public class Main {
    
    public static void main(String[] args) {
        
        Monkey m0 = new Monkey(0, (a -> a * 11), (i -> (i % 2 == 0)), 99, 63, 76, 93, 54, 73);
        Monkey m1 = new Monkey(1, (a -> a + 1), (i -> (i % 17 == 0)), 91, 60, 97, 54);
        Monkey m2 = new Monkey(2, (a -> a + 7), (i -> (i % 7 == 0)), 65);
        Monkey m3 = new Monkey(3, (a -> a + 3), (i -> (i % 11 == 0)), 84, 55);
        Monkey m4 = new Monkey(4, (a -> a * a), (i -> (i % 19 == 0)), 86, 63, 79, 54, 83);
        Monkey m5 = new Monkey(5, (a -> a + 4), (i -> (i % 5 == 0)), 96, 67, 56, 95, 64, 69, 96);
        Monkey m6 = new Monkey(6, (a -> a * 5), (i -> (i % 13 == 0)), 66, 94, 70, 93, 72, 67, 88, 51);
        Monkey m7 = new Monkey(7, (a -> a + 8), (i -> (i % 3 == 0)), 59, 59, 74);

        m0.setNextTrue(m7);
        m0.setNextFalse(m1);
        
        m1.setNextTrue(m3);
        m1.setNextFalse(m2);
        
        m2.setNextTrue(m6);
        m2.setNextFalse(m5);
        
        m3.setNextTrue(m2);
        m3.setNextFalse(m6);
        
        m4.setNextTrue(m7);
        m4.setNextFalse(m0);
        
        m5.setNextTrue(m4);
        m5.setNextFalse(m0);
        
        m6.setNextTrue(m4);
        m6.setNextFalse(m5);
        
        m7.setNextTrue(m1);
        m7.setNextFalse(m3);

        List<Monkey> monkeys = List.of(m0, m1, m2, m3, m4, m5, m6, m7);
        System.out.println(monkeys.toString());

        for(int i = 0; i < 10000; i++){
            for (Monkey monkey : monkeys) {
                // monkey.turn();
                monkey.turn2();
            }
        }

        long[] inspections1 = monkeys.stream()
        .mapToLong(m -> m.getInspections())
        .sorted()
        .toArray();
        System.out.println(inspections1.toString());
        System.out.println((inspections1[7] * inspections1[6]));



    }

}
