import java.util.Scanner;
import java.util.Random;

public class Q06{

    static String generateWord(String[] pWords)
    {
       // Fully completed function that generates and returns a secret word
       Random random = new Random();
       int randomNumber = random.nextInt(pWords.length); 
       String secretWord = pWords[randomNumber];
       return secretWord;
    } // End of generateWord subprogram

    // Add your subprograms here
    
   





// ---------------------------------------------------------------------------------------
// End of subprograms and start of main program from here

    public static void main(String[] args){
       
        // Array of words
        String[]  words = {"antelope","ape","badger","bear","beaver","bison","crocodile","elephant",
                           "elk","ferret","goat","goose","kangaroo","llama","lion","monkey","moose",
                           "orangutan","shark","snake","tiger","whale","wombat"};

        // Secret word is generated
        String wordToGuess = generateWord(words);

        // Add your main program code here
      




        
    } // End of main program
} // End of class