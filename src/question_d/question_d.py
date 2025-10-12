#write functions here, don't add input('') statements here!

def get_age():
    age = int(input("Enter your age: "))
    if age < 1:
        return "Infant"
    elif age >= 2 and age <= 13:
        return "Child"
    elif age >= 14 and age < 20:
        return "Teenager"
    elif age >= 20 and age < 65:
        return "Adult"
    elif age < 0 or age >= 125:
        return "Invalid age"


