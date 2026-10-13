# src/main.py
from utils import square, is_even, celsius_to_fahrenheit

def main():
    print("=== Python Lab Calculator ===")
    user_input = input("Enter a number: ")
    
    try:
        num = float(user_input)
        
        print(f"\nResults for input: {num}")
        print(f"- Square: {square(num)}")
        print(f"- Is Even? {is_even(num)}")
        print(f"- Fahrenheit equivalent (treating input as Celsius): {celsius_to_fahrenheit(num):.2f}°F")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
