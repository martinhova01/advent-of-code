package day7;

import java.util.ArrayList;
import java.util.List;

public class FileSystem {
    private Folder pointer;

    public FileSystem(){
        this.pointer = null;
    }

    public void cd(String name){
        if (name.equals("/")){
            this.pointer = new Folder("/", null);
        }
        else if (name.equals("..")){
            this.pointer = pointer.getParent();
        }
        else{
            this.pointer = pointer.getSubfolder(name);
        }
    }

    public void addFolder(String name){
        new Folder(name, pointer);
    }
    public void addFile(String name, int size){
        new File(name, pointer, size);
    }

    public Folder getPointer() {
        return pointer;
    }

    // public void printTree(){
    //     while (pointer.getParent() != null){
    //         this.cd("..");
    //     }
    //     pointer.printTree();
    // }

    public void setPointerToRootFolder(){
        while (pointer.getParent() != null){
            this.cd("..");
        }
    }

    public int getfolderSize(){
        return pointer.getSize();

    }

    public int getSumLessthan100000(Folder currentFolder){
        int sum = 0;
        
        if (currentFolder.getSize() < 100000){
            sum += currentFolder.getSize();
        }

        for (Folder folder : currentFolder.getSubFolders()){
            sum += this.getSumLessthan100000(folder);
        }

        return sum;

    }

    public List<Integer> getSums(Folder currentFolder, List<Integer> sums){

        sums.add(currentFolder.getSize());
        for (Folder folder : currentFolder.getSubFolders()){
            getSums(folder, sums);
        }

        return sums;
    }
}
