#add import
from question_d import get_age

def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age >= 125:
                print("Invalid age")
            elif age <= 1:
                print("Infant")
            elif age <= 13:
                print("Child")
            elif age >= 14 and age < 20:
                print("Teenager")
            else:
                print("Adult")
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
