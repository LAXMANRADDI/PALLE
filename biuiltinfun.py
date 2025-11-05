creatinga timer using simple while loop 

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


