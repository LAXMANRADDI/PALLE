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


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
simple use of if condn

a =[]
count=0
for i in range(0,11,2):
    a.append(i)
#print (a) 

for i in a :
    if i%2 == 0 :
        count+=1
        
if count >= 5:
    print ( ' limt reached') 

else :
    print ('got some space ')
