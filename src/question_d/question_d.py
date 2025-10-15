#write functions here, don't add input('') statements here!

def get_person_category(age):
    
    if not isinstance(age, int) or age < 0 or age > 124:
        return "Invalid age"
    if age <= 1:
        return "Infant"    
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 125:
        return "Adult"

def get_age(age):
    return get_person_category(age)
    print(f"Age 1: {get_person_category(5)}")
    print(f"Age 2: {get_person_category(15)}")
    print(f"Age 14: {get_person_category(30)}")
    print(f"Age 20: {get_person_category(70)}")
    print(f"Age 124: {get_person_category(124)}")


