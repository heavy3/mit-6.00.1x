def getSublists(L, n):
    '''
    takes as parameters a list of integers named L and an integer named n.
    assume L is not empty
    assume 0 < n <= len(L)
    returns a list of all possible sublists in L of length n without skipping elements in L
    '''
    # create a list to hold answer
    answer = []
    # iterate through list index
    for i in range(len(L) - n + 1):
        # create a list to hold n elements
        listn = []
        
        # add to listn n element form ith index
        for j in range(i, i + n):
            listn.append(L[j])
        
        # add listn as an object to answer
        answer.append(listn)
    
    # return answer
    return answer
    
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
print getSublists(L, n)
