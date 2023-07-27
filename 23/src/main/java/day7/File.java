package day7;

public class File {
    private String name;
    private Folder parent;
    private int size;

    public File(String name, Folder parent, int size){
        this.name = name;
        this.parent = parent;
        this.size = size;
        parent.addFile(this);
    }

    public  int getSize(){
        return this.size;
    }
}
