package day7;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class InputReader{
    
    static String getInput(String inputFileName){
        String result = "";
        InputStream is = InputReader.class.getResourceAsStream(inputFileName);
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
