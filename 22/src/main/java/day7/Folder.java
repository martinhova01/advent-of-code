package day7;

import java.util.ArrayList;
import java.util.List;

public class Folder {
    private String name;
    private Folder parent;
    private List<Folder> subFolders;
    private List<File> files;

    public Folder(String name, Folder parent){
        this.name = name;
        this.parent = parent;
        this.subFolders = new ArrayList<>();
        this.files = new ArrayList<>();
            //the new folder is the root of the filetree
        if (parent != null){
            parent.addSubFolder(this);
        }
    }

    public void addSubFolder(Folder subFolder){
        this.subFolders.add(subFolder);
    }

    public void addFile(File File){
        this.files.add(File);
    }

    public String getName(){
        return this.name;
    }

    public Folder getSubfolder(String name){
        Folder result = null;
        for(Folder folder : subFolders){
            if (folder.getName().equals(name)){
                result = folder;
            }
        }
        return result;
    }

    public Folder getParent(){
        return this.parent;
    }

    public int getSize(){
        int sum = 0;

        for (File file : files){
            sum += file.getSize();
        }

        for (Folder folder : subFolders){
            sum += folder.getSize();
        }

        return sum;
    }
    public List<Folder> getSubFolders() {
        return subFolders;
    }

    // public void printTree(){
        
    //     System.out.println(this.name);
    //     if (this.subFolders.size() != 0){
    //         for (Folder folder : subFolders) {
    //             folder.printTree();
    //         }
    //     }
    // }
}
