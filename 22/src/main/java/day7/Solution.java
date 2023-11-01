package day7;

import java.util.ArrayList;
import java.util.List;
import util.InputReader;

public class Solution {
    

    public static void main(String[] args) {
        String input = InputReader.getInput("../day7/day7.txt");
        FileSystem fileSystem = new FileSystem();
        boolean ls = false;

        for(String line : input.split("\n")){

            if (line.charAt(0) == '$'){
                //New command
                ls = false;
                String command = line.substring(2, 4);
                if (command.equals("cd")){
                    String dir = line.substring(5, line.length());
                    // System.out.println(dir);
                    fileSystem.cd(dir);
                }
                else if (command.equals("ls")){
                    ls = true;
                }
            }
            else if (ls){
                //execute command
                String[] element = line.split(" ");
                if (element[0].equals("dir")){
                    String folderName = element[1];
                    fileSystem.addFolder(folderName);
                }
                else{
                    int size = Integer.parseInt(element[0]);
                    String fileName = element[1];
                    fileSystem.addFile(fileName, size);
                }
            }
        }
        
        
            //Part 1
        fileSystem.setPointerToRootFolder();
        // System.out.println(fileSystem.getSumLessthan100000(fileSystem.getPointer()));


        int totalDiskSpace = 70000000;
        int usedSpace = fileSystem.getPointer().getSize();

        int avalibleSpace = totalDiskSpace - usedSpace;

        int spaceNeeded = 30000000 - avalibleSpace;
        // System.out.println(spaceNeeded);

        fileSystem.setPointerToRootFolder();
        List<Integer> possibleSpaceSavings = fileSystem.getSums(fileSystem.getPointer(), new ArrayList<>());
        // System.out.println(possibleSpaceSavings);

        int smallest = 1000000000;
        for (Integer sum : possibleSpaceSavings) {
            if (sum < smallest && sum > spaceNeeded){
                smallest = sum;
            }
        }
        
        System.out.println(smallest);



    }
}
