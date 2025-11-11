creating a timer using simple while loop 

import time # import time from sys
x = input (int ()) # time in seconds 
while x>= 1:
  print(x)
  time.sleep(1 , flush ==True) # sleep is used create delay in printng ouput  and flush here is not recomended , is used to print output immidiatly 
  x -= 1 # decrement
print (" time up ")

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
some use cases of split() function
s = 'palle technology'
r =  s.split() #   [ 'palle' , 'technology']
r= s.spit('') # throws error since seperator is not defined
r = s.split('e', 1) # ['pall' , ' technology']
r= s.split('e', 2) # ['pall' , ' t' , 'chnology'] 
r= s.split ('l') # ['pa', '', 'e techno', 'ogy']


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
practice problems related to ascii conversions 
*] simple problem related to conversion of given charectors in list to another case and vice versa 
l1 = ['a', 'A', 'c', 'G']
l2 = []

for i in l1:
    if 'A' <= i <= 'Z':        # uppercase → lowercase
        l2.append(chr(ord(i) + 32))
    elif 'a' <= i <= 'z':      # lowercase → uppercase
        l2.append(chr(ord(i) - 32))

print(l2)
