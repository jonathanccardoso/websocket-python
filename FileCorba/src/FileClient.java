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
import java.util.*;
import org.omg.CosNaming.*;
import org.omg.CORBA.*;

public class FileClient {
    public static void main(String argv[]) {
        try {
            // create and initialize the ORB
            ORB orb = ORB.init(argv, null);
            // get the root naming context
            org.omg.CORBA.Object objRef =
                orb.resolve_initial_references("NameService");
            NamingContext ncRef = NamingContextHelper.narrow(objRef);
            NameComponent nc = new NameComponent("FileTransfer", " "); 
            // Resolve the object reference in naming
            NameComponent path[] = {nc};
            FileInterfaceOperations fileRef =
                FileInterfaceHelper.narrow(ncRef.resolve(path));

            if(argv.length < 1) {
                System.out.println("Usage: java FileClient filename");
            }

            // save the file
            File file = new File(argv[0]);
            byte data[] = fileRef.downloadFile(argv[0]);
            BufferedOutputStream output = new
            BufferedOutputStream(new FileOutputStream(argv[0]));
            output.write(data, 0, data.length);
            output.flush();
            output.close();
            System.out.println("File " + argv[0] + " transfered!");
        } catch(Exception e) {
            System.out.println("FileClient Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
