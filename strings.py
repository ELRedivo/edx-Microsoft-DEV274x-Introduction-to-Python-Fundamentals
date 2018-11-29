#Invert String
def invert_string(string):
    
    inverted_string = ''
    counter = -1
    
    while counter > (-(len(string)) - 1):
    
        inverted_string += string[counter]
        counter += -1
    
    return inverted_string