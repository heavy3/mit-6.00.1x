def longestRun(L):
    '''
    takes as a parameter a list of integers named L (assume L is not empty)
    returns the length of the longest run of monotonically increasing numbers occurring in L
    A run of monotonically increasing numbers means that a number at position k+1 
    in the sequence is either greater than or equal to the number at position k in the sequence.
    '''
    # the longest run is set to be 1
    longest = 1
    
    # iterate through list, 
    for i in range(len(L)):
        # create a temp mono run
        temp = 1
        
        # find the longest
        for j in range(i, len(L) - 1):
            if L[j] <= L[j+1]:
                temp +=1
            else: 
                break
        
        # compare temp and longest
        if temp > longest:
            longest = temp
    # the result
    return longest

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]        
print longestRun(L)