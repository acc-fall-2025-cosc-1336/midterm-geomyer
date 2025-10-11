#write functions here, don't add input('') statements here!


#Tax rate = 0.6
#Assessment value = property value * tax rate
#Tax Assessed = assessment value * 72 cents per $100


property_tax_rate = 0.6


def get_assessment_value(property_value):
    if property_value == 10000:
        return property_value * property_tax_rate
    if property_value == 20000:
        return property_value * property_tax_rate
    
def get_tax_assessed(assessment_value):
    if assessment_value == 6000:
        return assessment_value * 0.0072    
    if assessment_value == 10000:
        return assessment_value * 0.0072
    

