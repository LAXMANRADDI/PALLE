ternanry condition for checking greatest of three numbres 
a ,b ,c =10 ,20,30
print (f'{a} is largest ' if a>b and a>c else(f'{b} is greater' if b>c  else f' {c} is largest ')) 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   trenary with  help of tuples 

x = int ( input ('entr age: ') )
res = ('is not adult ' , 'is adult ')[x >= 18]
print (res)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
 with dictionary 


x = int ( input ('entr age: ') )
res = {False :'is not adult ' , True :'is adult '}[x >= 18]
print (res)
