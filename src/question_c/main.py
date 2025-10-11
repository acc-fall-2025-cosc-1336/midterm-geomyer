#add import
from question_c import get_assessment_value, get_tax_assessed

def main():
    #get property value from user
    property_value = float(input("Enter the property value: "))
    
    #call get_assessment_value function
    assessment_value = get_assessment_value(property_value)
    
    #call get_tax_assessed function
    tax_assessed = get_tax_assessed(assessment_value)
    
    #print assessment value and tax assessed, formatted to 2 decimal places
    print(f"Assessment Value: ${assessment_value:.2f}")
    print(f"Tax Assessed: ${tax_assessed:.2f}")

    while True:
        another = input("Do you want to enter another property value? (yes/no): ").strip().lower()
        if another == 'yes':
            property_value = float(input("Enter the property value: "))
            assessment_value = get_assessment_value(property_value)
            tax_assessed = get_tax_assessed(assessment_value)
            print(f"Assessment Value: ${assessment_value:.2f}")
            print(f"Tax Assessed: ${tax_assessed:.2f}")
        elif another == 'no':
            print("Exiting the program.")
            break
        else:
            print("Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    main()
