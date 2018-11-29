# write a function that takes your name
# and returns the first and the last characters of your name
# e.g. Chukwudi becomes Ci

def first_last(name):
    myname = name
    first_last_char = myname[:1]+myname[-1]
    return first_last_char


your_name = input('Please enter your first name ')
print(first_last(your_name))