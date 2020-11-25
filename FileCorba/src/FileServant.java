/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author laura
 */
import java.io.*; 
import org.omg.CORBA.ORB;

public class FileServant extends FileInterfacePOA {
    private ORB orb;
    
    public void setORB(ORB orb_val){
        orb = orb_val;
    }
    
    public byte[] downloadFile(String fileName){
        File file = new File(fileName);
        byte buffer[] = new byte[(int)file.length()];
        try {
            BufferedInputStream input = new
            BufferedInputStream(new FileInputStream(fileName));
            input.read(buffer,0,buffer.length);
            input.close();
        } catch(Exception e) {
            System.out.println("FileServant Error: "+e.getMessage());
            e.printStackTrace();
        }
        System.out.println("Transfering file " + fileName + " ...");
        return(buffer); 
    }
}
