#!/usr/bin/env python3
"""
ASCII Art Text Generator
Converts regular text into fun ASCII block letters!
"""

def get_ascii_art():
  """Returns a dictionary mapping characters to ASCII art representations"""
  return {
    'A': [
      "  ██  ",
      " ████ ",
      "██  ██",
      "██████",
      "██  ██"
    ],
    'B': [
      "██████",
      "██  ██",
      "██████",
      "██████",
      "██████"
    ],
    'C': [
      " █████",
      "██    ",
      "██    ",
      "██    ",
      " █████"
    ],
    'D': [
      "██████",
      "██  ██",
      "██  ██",
      "██  ██",
      "██████"
    ],
    'E': [
      "██████",
      "██    ",
      "██████",
      "██    ",
      "██████"
    ],
    'F': [
      "██████",
      "██    ",
      "██████",
      "██    ",
      "██    "
    ],
    'G': [
      " █████",
      "██    ",
      "██ ███",
      "██  ██",
      " █████"
    ],
    'H': [
      "██  ██",
      "██  ██",
      "██████",
      "██  ██",
      "██  ██"
    ],
    'I': [
      "██████",
      "  ██  ",
      "  ██  ",
      "  ██  ",
      "██████"
    ],
    'J': [
      "██████",
      "    ██",
      "    ██",
      "██  ██",
      " █████"
    ],
    'K': [
      "██  ██",
      "██ ██ ",
      "████  ",
      "██ ██ ",
      "██  ██"
    ],
    'L': [
      "██    ",
      "██    ",
      "██    ",
      "██    ",
      "██████"
    ],
    'M': [
      "██  ██",
      "██████",
      "██████",
      "██  ██",
      "██  ██"
    ],
    'N': [
      "██  ██",
      "███ ██",
      "██████",
      "██ ███",
      "██  ██"
    ],
    'O': [
      " █████",
      "██  ██",
      "██  ██",
      "██  ██",
      " █████"
    ],
    'P': [
      "██████",
      "██  ██",
      "██████",
      "██    ",
      "██    "
    ],
    'Q': [
      " █████",
      "██  ██",
      "██  ██",
      "██ ███",
      " ██████"
    ],
    'R': [
      "██████",
      "██  ██",
      "██████",
      "██ ██ ",
      "██  ██"
    ],
    'S': [
      " █████",
      "██    ",
      " █████",
      "    ██",
      "█████ "
    ],
    'T': [
      "██████",
      "  ██  ",
      "  ██  ",
      "  ██  ",
      "  ██  "
    ],
    'U': [
      "██  ██",
      "██  ██",
      "██  ██",
      "██  ██",
      " █████"
    ],
    'V': [
      "██  ██",
      "██  ██",
      "██  ██",
      " ████ ",
      "  ██  "
    ],
    'W': [
      "██  ██",
      "██  ██",
      "██████",
      "██████",
      "██  ██"
    ],
    'X': [
      "██  ██",
      " ████ ",
      "  ██  ",
      " ████ ",
      "██  ██"
    ],
    'Y': [
      "██  ██",
      " ████ ",
      "  ██  ",
      "  ██  ",
      "  ██  "
    ],
    'Z': [
      "██████",
      "   ██ ",
      "  ██  ",
      " ██   ",
      "██████"
    ],
    ' ': [
      "      ",
      "      ",
      "      ",
      "      ",
      "      "
    ]
  }

def text_to_ascii(text):
  """Convert text string to ASCII art"""
  ascii_dict = get_ascii_art()
  text = text.upper()
  
  # Initialize 5 lines for the output
  lines = ["", "", "", "", ""]
  
  for char in text:
    if char in ascii_dict:
      char_art = ascii_dict[char]
      for i in range(5):
        lines[i] += char_art[i] + " "
    else:
      # For unsupported characters, add spaces
      for i in range(5):
        lines[i] += "      "
  
  return '\n'.join(lines)

def main():
  """Main function to run the ASCII art generator"""
  print("🎨 ASCII Art Text Generator 🎨")
  print("=" * 40)
  
  while True:
    try:
      text = input("\nEnter text to convert (or 'quit' to exit): ").strip()
      
      if text.lower() == 'quit':
        print("Thanks for using the ASCII Art Generator! 👋")
        break
      
      if not text:
        print("Please enter some text!")
        continue
      
      if len(text) > 15:
        print("Text too long! Please keep it under 15 characters.")
        continue
      
      print("\n" + "=" * 50)
      print(text_to_ascii(text))
      print("=" * 50)
      
    except KeyboardInterrupt:
      print("\n\nGoodbye! 👋")
      break
    except Exception as e:
      print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()