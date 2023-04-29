package day14;

public class Main {

    static boolean part1 = false;

    public static void main(String[] args) {
        String input = InputReader.getInput("input.txt");
        String[] lines = input.split("\n");

        Grid g = new Grid(200, 500);
        int largestY = 0;

        for(String line : lines){
            String[] coordinates = line.split(" -> ");

            int x = Integer.parseInt(coordinates[0].split(",")[0]) - 200;
            int y = Integer.parseInt(coordinates[0].split(",")[1]);
            if(y > largestY){largestY = y;}

            for(int i = 1; i < coordinates.length; i++){
                int nextX = Integer.parseInt(coordinates[i].split(",")[0]) - 200;
                int nextY = Integer.parseInt(coordinates[i].split(",")[1]);
                if(nextY > largestY){largestY = nextY;}

                int directionX;
                int directionY;

                if (x == nextX){
                    directionX = 0;
                    if (y < nextY){
                        directionY = 1;
                    }
                    else{
                        directionY = -1;
                    }
                }
                else{
                    directionY = 0;
                    if (x < nextX){
                        directionX = 1;
                    }
                    else{
                        directionX = -1;
                    }
                }
                g.replace(x, y, '#');
                while (!(x == nextX && y == nextY)){
                    x += directionX;
                    y += directionY;
                    g.replace(x, y, '#');
                }
            }
        }

        if(part1){
            while(!g.isFinished()){
                if(!g.moveSand()){
                    g.spawnSand();
                }
            }
            g.print();
            System.out.println("Part 1: " + g.countSand());
        }
        else{
            for(int x = 0; x < 500; x++){
                g.replace(x, largestY + 2, '#');
            }

            while(!g.isFinished()){
                if(!g.moveSand()){
                    g.spawnSand();
                }
            }
            g.print();
            System.out.println("Part 2: " + g.countSand());
        }

        
    }

    
    
}
