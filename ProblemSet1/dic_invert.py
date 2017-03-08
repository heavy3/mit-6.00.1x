def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    # create a dictionary to hold invert list
    invert = {}
    
    # iterate through d in key
    for key1 in d.keys():
        
        # create a list to hold key
        value = []
        value.append(key1)
        
        # find more key with the same value
        for key2 in d.keys():
            
            # check if that value is the same in different key
            if d[key1] == d[key2] and key1 != key2:
                value.append(key2)
        
        # sort the list
        value.sort()
        
        # add an invert key-value pair to invert list
        invert[d[key1]] = value
        
    # return the invert dict
    return invert
    
d = {4:True, 2:True, 0:True}
print dict_invert(d)
            