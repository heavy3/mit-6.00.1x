s = 'bobobobobobobobob'

sub = 'bob'
pos = -1
count = 0
while True:
   newpos = s[pos + 1:].find(sub)
   print 'newpos' +str(newpos)
   if newpos == -1:
       break
   elif newpos == 0 and count != 0:
       newpos = 1 
   else:
        count += 1
   pos += newpos 
   print 'pos' + str(pos)     
print 'Number of times bob occurs is: ' + str(count)
    