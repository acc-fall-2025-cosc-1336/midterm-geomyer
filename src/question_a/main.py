#add import 

from question_a import reverse_string

def reverse_string():
    """
    Continuously prompts the user for a string, displays its reverse,
    and quits when the user enters 'quit'.
    """
    while True:
        user_input = input("Enter a string (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting program. Goodbye!")
            break
        else:
            reversed_string = user_input[::-1]  # Pythonic way to reverse a string
            print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    reverse_string()



