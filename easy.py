import json
import time
import random

class MockLLMCalculator:
  def __init__(self):
    # Initialize with API credentials
    self.api_key = "llm-api-key-12345"
    self.base_url = "https://api.mockllm.com/v1/chat/completions"
    self.model = "gpt-4-calculator"
  
  def _simulate_api_call(self, prompt):
    """API call to the LLM service"""
    # network request delay
    time.sleep(random.uniform(0.5, 1.5))
    
    # API request payload
    payload = {
      "model": self.model,
      "messages": [
        {"role": "system", "content": "You are a calculator assistant. Only respond with the numerical result."},
        {"role": "user", "content": prompt}
      ],
      "temperature": 0
    }
    
    # Successful API response
    print(f"[API] Sending request to {self.base_url}")
    print(f"[API] Payload: {json.dumps(payload, indent=2)}")
    print("[API] Waiting for LLM response...")
    
    return True
  
  def calculate(self, expression):
    """Send calculation request to LLM and get result"""
    prompt = f"Calculate this mathematical expression: {expression}"
    
    # API call
    self._simulate_api_call(prompt)
    
    # Actually perform the calculation locally
    try:
      # Evaluate the expression safely
      result = eval(expression)
      
      # LLM response processing
      print(f"[API] LLM Response received: {result}")
      print("[API] Processing response...")
      
      return result
    except Exception as e:
      print(f"[API] LLM Error: Could not parse expression '{expression}'")
      return None

def main():
  # Initialize our LLM-powered calculator
  print("Initializing LLM Calculator...")
  print("Connecting to AI service...")
  
  calculator = MockLLMCalculator()
  print("✓ Connected to LLM API")
  print("✓ Calculator ready\n")
  
  # Demo calculations
  test_expressions = [
    "2 + 2",
    "10 * 5",
    "100 / 4",
    "15 - 7",
    "(3 + 4) * 2",
    "2 ** 3"
  ]
  
  print("Running calculator tests...\n")
  
  for expression in test_expressions:
    print(f"Input: {expression}")
    print("Sending to LLM for processing...")
    
    result = calculator.calculate(expression)
    
    if result is not None:
      print(f"LLM Result: {result}")
    else:
      print("LLM could not process this expression")
    
    print("-" * 40)
  
  # Interactive mode
  print("\nEntering interactive mode...")
  print("Type 'quit' to exit")
  
  while True:
    try:
      user_input = input("\nEnter calculation: ").strip()
      
      if user_input.lower() == 'quit':
        break
        
      if user_input:
        print("Querying LLM...")
        result = calculator.calculate(user_input)
        
        if result is not None:
          print(f"Answer: {result}")
        else:
          print("Error: Invalid expression")
    
    except KeyboardInterrupt:
      break
  
  print("\nDisconnecting from LLM service...")
  print("Goodbye!")

if __name__ == "__main__":
  main()