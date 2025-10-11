#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):
    reversed_str = ""
    i = len(string1) - 1
    while i >= 0:
        reversed_str += string1[i]
        i -= 1
    return reversed_str
print(reverse_string("Hello World"))    

