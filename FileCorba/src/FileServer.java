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
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import org.omg.PortableServer.*;
import org.omg.PortableServer.POA;

public class FileServer {
    public static void main(String args[]) {
        try{
            // create and initialize the ORB
            ORB orb = ORB.init(args, null);
            // create the servant and register it with the ORB
            FileServant fileRef = new FileServant();
            fileRef.setORB(orb);
            // get the root naming context; returns a generic CORBA object
            org.omg.CORBA.Object objRef =
                orb.resolve_initial_references("NameService");
            // cast (narrow down) the reference to the root of the naming
            // service (a generic CORBA object) to its proper type
            NamingContext ncRef = NamingContextHelper.narrow(objRef);
            
            //Obtém referência a rootpoa (Portable Object Adapter) e ativa o gerenciador POA 
            POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate();
            
            org.omg.CORBA.Object ref = rootpoa.servant_to_reference(fileRef);
            FileInterface href = FileInterfaceHelper.narrow(ref);
            
            // Bind the object reference in naming
            NameComponent nc = new NameComponent("FileTransfer", " ");
            NameComponent path[] = {nc};
            ncRef.rebind(path, href);
            System.out.println("Server started....");
            // Wait for invocations from clients
            java.lang.Object sync = new java.lang.Object();
            synchronized(sync){
                sync.wait();
            }
        } catch(Exception e) {
            System.err.println("ERROR: " + e.getMessage());
            e.printStackTrace(System.out);
        }
    }
}
