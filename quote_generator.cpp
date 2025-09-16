#include <iostream>  // For input/output operations (std::cout, std::cin)
#include <vector>    // For std::vector container to store collections of strings
#include <string>    // For std::string class to handle text data
#include <random>    // For random number generation facilities
#include <ctime>     // For time-related functions (though not used in this version)

// Pre-defined database of quote parts - these vectors store the building blocks for quotes

// Collection of subjects that quotes can be about
// These represent the main topic or focus of the inspirational quote
std::vector<std::string> subjects = {
  "Success", "Happiness", "Life", "Dreams", "Courage", "Wisdom", "Love", "Hope", "Failure", "Change"
};

// Collection of verbs/actions that connect subjects to objects
// These create the relationship between the subject and what follows
std::vector<std::string> verbs = {
  "is", "comes from", "begins with", "requires", "demands", "creates", "destroys", "transforms", "builds", "reveals"
};

// Collection of objects/concepts that complete the main thought
// These represent actions, states, or concepts that relate to the subject
std::vector<std::string> objects = {
  "hard work", "determination", "believing in yourself", "taking risks", "learning from mistakes", 
  "helping others", "never giving up", "embracing change", "following your passion", "staying positive"
};

// Collection of ending phrases to complete the quote
// These add philosophical or motivational closure to the quote
std::vector<std::string> endings = {
  "and nothing else matters.", "when you least expect it.", "in the darkest moments.",
  "through perseverance.", "with an open heart.", "against all odds.", "one step at a time.",
  "when you stop making excuses.", "in the journey, not the destination.", "by staying true to yourself."
};

// Function to generate a random inspirational quote
// Combines random elements from each vector to create unique quotes
// Returns: A complete quote as a string
std::string generateRandomQuote() {
  // Static random device - initializes once and persists between function calls
  // Used to seed the random number generator with entropy from hardware
  static std::random_device rd;
  
  // Static Mersenne Twister generator - high-quality random number generator
  // Seeded with the random device, static ensures it persists between calls
  static std::mt19937 gen(rd());
  
  // Create uniform distribution for subjects vector
  // Generates random indices from 0 to (subjects.size() - 1)
  std::uniform_int_distribution<> subjectDist(0, subjects.size() - 1);
  
  // Create uniform distribution for verbs vector
  // Generates random indices from 0 to (verbs.size() - 1)
  std::uniform_int_distribution<> verbDist(0, verbs.size() - 1);
  
  // Create uniform distribution for objects vector
  // Generates random indices from 0 to (objects.size() - 1)
  std::uniform_int_distribution<> objectDist(0, objects.size() - 1);
  
  // Create uniform distribution for endings vector
  // Generates random indices from 0 to (endings.size() - 1)
  std::uniform_int_distribution<> endingDist(0, endings.size() - 1);
  
  // Construct the quote by concatenating randomly selected elements
  // Format: [Subject] [Verb] [Object] [Ending]
  // Each distribution generates a random index, used to select from respective vector
  std::string quote = subjects[subjectDist(gen)] + " " +     // Random subject + space
             verbs[verbDist(gen)] + " " +                    // Random verb + space
             objects[objectDist(gen)] + " " +                // Random object + space
             endings[endingDist(gen)];                       // Random ending (no space after)
  
  // Return the completed quote string to the caller
  return quote;
}

// Main function - entry point of the program
// Handles user interaction and program flow control
int main() {
  // Display program title with decorative formatting
  std::cout << "Random Quote Generator\n";
  std::cout << "======================\n\n";
  
  // Declare variable to store user's choice for continuing or exiting
  char choice;
  
  // Main program loop - continues until user chooses to exit
  do {
    // Generate and display a new random quote with quotation marks for formatting
    std::cout << "\"" << generateRandomQuote() << "\"\n\n";
    
    // Prompt user for input to continue or exit the program
    std::cout << "Generate another quote? (y/n): ";
    
    // Read user's choice from standard input
    std::cin >> choice;
    
    // Add blank line for better visual formatting
    std::cout << "\n";
    
  // Loop continues if user enters 'y' or 'Y' (case-insensitive yes)
  // Loop exits for any other input (including 'n', 'N', or invalid input)
  } while (choice == 'y' || choice == 'Y');
  
  // Display farewell message when user chooses to exit
  std::cout << "Thank you for using the Random Quote Generator!\n";
  
  // Return 0 to indicate successful program execution to the operating system
  return 0;
}