def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''  
    if type(aList) == list:
        # flatten
        newList = []
        for item in aList:
            flattenned = flatten(item)
            # extend will iterate each item, so not good for obj type int or str
            if type(flattenned) == list:
                newList.extend(flattenned)
            else:
                newList.append(flattenned)
        return newList
    else:
        return aList


aList = [[[1]], [[[5]]]]
print flatten(aList)
