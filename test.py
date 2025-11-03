
############################################# GCD of two number euclid's gcd algorithm .. considering 1st entered number is greater than second number
n1 = int (input('enter n1:'))
n2 = int (input('enter num 2:'))

while n1 % n2 != 0:
    r = n1%n2
    n1 = n2
    n2 = r
print('gcd is:',n2) 
OUTPUT1:
enter n1:120
enter num 2:20
gcd is: 20

OUTPUT2:
enter n1:7
enter num 2:33
gcd is: 1

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
greatest of given numbers by index based operation 

l = [10,20,30,40,50,60,70,80,90,100]
a =l [0]
for i in range (1,len(l)):
    if l[i]>a:
        a = l[i]
print(f'largest is:{a}')
OUTPUT:
largest is:100


%%%%%%%%%%%%%%%%%%%%%
by fetching values in list 
l = list(map(int , input('enter numbers with space').split()))    
a =l [0]
for i in l:
    if i>a:
        a = i
print(f'largest is:{a}') 

OUTPUT:
enter numbers with space10 50 40 77 88 99 22 11 111
largest is:111




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n =int (input('ENTER N:'))
count =0
while n>0:
    n=n//10
    count+=1
print(f'number of digits:{count}')

output 1:
ENTER N:15245645282648265
number of digits:17

output2:
ENTER N:0000000000000000000000000001
number of digits:1

######################################################

