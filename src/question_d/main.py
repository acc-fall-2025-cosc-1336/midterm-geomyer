#add import
from question_d import get_person_category

def main():
    while True:
        try:
            user_input = int(input("Enter your age: "))
            if user_input < 0:
                print("Invalid Input.")
                break
            category = get_person_category(user_input)
            print(f"Age {user_input} is categorized as: {category}")
        except ValueError:
            print("Please enter a valid integer for age.")  
        again = input("Do you want to check another age? (y/n): ").strip().lower()
        if again == 'n':
            print("Goodbye!")
            break
        elif again != 'y':
            print("Invalid input. Please enter 'y' or 'n'.") 


if __name__ == "__main__":
    
    main()