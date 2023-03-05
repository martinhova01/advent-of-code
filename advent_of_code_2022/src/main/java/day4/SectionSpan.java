package day4;

public class SectionSpan {
    private int startsection;
    private int endsection;

    public SectionSpan(int startsection, int endsection) {
        this.startsection = startsection;
        this.endsection = endsection;
    }

    public boolean contains(SectionSpan other){
        if (this.startsection <= other.startsection && this.endsection >= other.endsection){
            return true;
        }
        return false;
    }

    public boolean overlaps(SectionSpan other){
        if ((other.startsection <= this.endsection && other.endsection >= this.endsection)
         || (other.endsection >= this.startsection && other.startsection <= this.startsection)){
            return true;
        }
        return false;
    }

    
}
