def isvowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    return False
    
count = 0
for char in s:
    if isvowel(char):
        count += 1
print 'Number of vowels:' + str(count)