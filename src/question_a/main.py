#add import 

from question_a import reverse_string_no_slice


def main():
    user_input = input("Enter a string to reverse: ")
    reversed_string = reverse_string_no_slice(user_input)
    print("Reversed string:", reversed_string)
    while True:
        again = input("Do you want to reverse another string? (y/n): ").strip().lower()
        if again == 'y':
            user_input = input("Enter a string to reverse: ")
            reversed_string = reverse_string_no_slice(user_input)
            print("Reversed string:", reversed_string)
        elif again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    


if __name__ == "__main__":
    main()

