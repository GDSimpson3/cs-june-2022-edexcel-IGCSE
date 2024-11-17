import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;

public class Q05a{
    
    public static void main(String[] args) throws FileNotFoundException {
       
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Valid uppercase letters in the alphabet
        String digit = "0123456789"; // Valid digits

        /*  Replace 'C:\\Users\\Pearson\\Data\\' in line 15 with the 
        	full path for your exam folder in your system */
        String path = "C:\\Users\\Pearson\\Data\\";
        String passwordFile = path + "passwords.txt";

        //	Open passwords.txt as input
        Scanner theFile = new Scanner(new BufferedReader(new FileReader(passwordFile)));

         // Add your code here 
       



         
    } // End of main program
} // End of class