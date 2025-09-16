#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <ctime>

// Pre-defined database of quote parts
std::vector<std::string> subjects = {
  "Success", "Happiness", "Life", "Dreams", "Courage", "Wisdom", "Love", "Hope", "Failure", "Change"
};

std::vector<std::string> verbs = {
  "is", "comes from", "begins with", "requires", "demands", "creates", "destroys", "transforms", "builds", "reveals"
};

std::vector<std::string> objects = {
  "hard work", "determination", "believing in yourself", "taking risks", "learning from mistakes", 
  "helping others", "never giving up", "embracing change", "following your passion", "staying positive"
};

std::vector<std::string> endings = {
  "and nothing else matters.", "when you least expect it.", "in the darkest moments.",
  "through perseverance.", "with an open heart.", "against all odds.", "one step at a time.",
  "when you stop making excuses.", "in the journey, not the destination.", "by staying true to yourself."
};

std::string generateRandomQuote() {
  static std::random_device rd;
  static std::mt19937 gen(rd());
  
  std::uniform_int_distribution<> subjectDist(0, subjects.size() - 1);
  std::uniform_int_distribution<> verbDist(0, verbs.size() - 1);
  std::uniform_int_distribution<> objectDist(0, objects.size() - 1);
  std::uniform_int_distribution<> endingDist(0, endings.size() - 1);
  
  std::string quote = subjects[subjectDist(gen)] + " " + 
             verbs[verbDist(gen)] + " " + 
             objects[objectDist(gen)] + " " + 
             endings[endingDist(gen)];
  
  return quote;
}

int main() {
  std::cout << "Random Quote Generator\n";
  std::cout << "======================\n\n";
  
  char choice;
  do {
    std::cout << "\"" << generateRandomQuote() << "\"\n\n";
    std::cout << "Generate another quote? (y/n): ";
    std::cin >> choice;
    std::cout << "\n";
  } while (choice == 'y' || choice == 'Y');
  
  std::cout << "Thank you for using the Random Quote Generator!\n";
  return 0;
}