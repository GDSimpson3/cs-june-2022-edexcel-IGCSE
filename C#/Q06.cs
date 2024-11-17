using System;

namespace Q06
{
    class Program
    {
        static string generateWord(string[] pWords)
        {
           // Fully completed function that generates and returns a secret word
           Random random = new Random();
           int randomNumber = random.Next(0,pWords.Length - 1); 
           string secretWord = pWords[randomNumber];
           return secretWord;
        } // End of generateWord subprogram

        // Add your subprograms here
        





// ---------------------------------------------------------------------------------------
// End of subprograms and start of main program from here

        static void Main(string[] args)
        {
            // Array of words
            string[]  words = {"antelope","ape","badger","bear","beaver","bison","crocodile","elephant",
                              "elk","ferret","goat","goose","kangaroo","llama","lion","monkey","moose",
                              "orangutan","shark","snake","tiger","whale","wombat"};

            // Secret word is generated
            string wordToGuess = generateWord(words);

            // Add your main program code here
           




           
        } // End of main 
    } // End of program
} // End of namespace