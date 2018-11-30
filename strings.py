#Invert String
def invert_string(string):
    
    inverted_string = ''
    counter = -1
    
    while counter > (-(len(string)) - 1):
    
        inverted_string += string[counter]
        counter += -1
    
    return inverted_string

#Slice String
def slice_string(string,start,stop):

    sliced_string = ''
    
    while start < stop:

        sliced_string += string[start]
        start += 1
    
    return sliced_string

#Some things
iterable = '12345'
mul_iterables = ''

counter_iterable = 1
size_iterable = len(iterable)

for item in iterable:
    
    mul_iterables += item
    
    if counter_iterable == size_iterable:
        break
    else:
        #Separator of strings
        mul_iterables += '-'
        counter_iterable += 1
    
print(mul_iterables)