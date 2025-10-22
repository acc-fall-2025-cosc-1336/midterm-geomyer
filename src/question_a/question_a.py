#write functions here, don't add input('') statements here!
# Reverse string without slicing to print hello world


def reverse_string_no_slice(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string_no_slice("Hello World"))


