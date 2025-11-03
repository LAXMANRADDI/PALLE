
############################################# GCD of two number euclid's gcd algorithm .. considering 1st entered number is greater than second number
n1 = int (input('enter n1:'))
n2 = int (input('enter num 2:'))

while n1 % n2 != 0:
    r = n1%n2
    n1 = n2
    n2 = r
print('gcd is:',n2)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
greatest of given numbers by index based operation 

l = [10,20,30,40,50,60,70,80,90,100]
a =l [0]
for i in range (1,len(l)):
    if l[i]>a:
        a = l[i]
print(f'largest is:{a}')



%%%%%%%%%%%%%%%%%%%%%
by fetching values in list 
l = [10,20,30,40,50,60,70,80,90,100]
a =l [0]
for i in l:
    if i>a:
        a = i
print(f'largest is:{a}') 








