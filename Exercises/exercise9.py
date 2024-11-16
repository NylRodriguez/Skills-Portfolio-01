# Define a function called 'hello' that prints "Hello"
def hello():
    print("Hello")  # This will output the string "Hello" when the function is called

# Define the main function that will call the 'hello' function
def main():
    hello()  # This calls the 'hello' function, which prints "Hello"

# This conditional checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":  
    main()  # If the script is run directly, it will call the 'main' function, which in turn calls 'hello'
