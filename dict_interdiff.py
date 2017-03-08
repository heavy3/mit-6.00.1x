def f(a, b):
    return a > b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = {}
    different = {}
    for key in d1.iterkeys():
        if d2.has_key(key):
            temp = {key: f(d1[key], d2[key])}
            intersect.update(temp)
        else:
            different.update({key: d1[key]})
    for key in d2.iterkeys():
        if not d1.has_key(key):
            different.update({key: d2[key]})
    t = (intersect, different)
    return t

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1, d2)