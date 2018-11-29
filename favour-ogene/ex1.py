# create a function that takes in a string as an input and repeats that string in 3 places
# e.g. boy becomes boyboy.
# note that you are to do a string multiplication


def multiple_string(string):
    newstr = string * 3
    return newstr


newinput = input('Enter a string ')

print(multiple_string(newinput))
