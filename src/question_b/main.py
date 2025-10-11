#add import 

from question_b import is_prime

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    while True:
        again = input("Do you want to check another number? (y/n): ").strip().lower()
        if again == 'y':
            num = int(input("Enter a number: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        elif again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
if __name__ == "__main__":
    main()