from helper1 import greet
from helper2 import add_numbers

def main():
    print("Welcome to My Python Project!")
    
    # Call greet function from helper1.py
    greet("Alice")
    
    # Call add_numbers function from helper2.py
    result = add_numbers(5, 3)
    print(f"The sum of 5 and 3 is {result}")

if __name__ == "__main__":
    main()
