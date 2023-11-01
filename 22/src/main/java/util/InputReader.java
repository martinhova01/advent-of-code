package util;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class InputReader{
    
    public static String getInput(String inputPathString){
        String result = "";
        InputStream is = InputReader.class.getResourceAsStream(inputPathString);
        BufferedReader br = new BufferedReader( new InputStreamReader(is));
        try{
            while(br.ready()){
                result += br.readLine() + "\n";
            }
        }
        catch(Exception e){e.printStackTrace();}

        return result;
    }
}
