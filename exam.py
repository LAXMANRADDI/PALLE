%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 

a= -10 
for i in range (-10,11):
    print(i , end=',')
-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,
%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
a= -10 
while a<=10:
    print(a , end=',')
    a+=1 

-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,

$$$$$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
using end = " " class


for i in range(1,16):
    if i%5!=0:
        print(i , end='@')
    else:
        print(i )
1@2@3@4@5
6@7@8@9@10
11@12@13@14@15 


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
factorial

n=int(input())
fact =1
while n!=0:
 fact=fact*n
 n-=1
print(fact) 

output1:
9
362880
 
output2:
0
1 

##########################################
palindrome check

m = int(input('Enter a number: '))
n = m  
s = 0   

while m > 0:
    r = m % 10     
    s = s * 10 + r 
    m = m // 10    

if n == s:
    print('Number is a palindrome')
else:
    print('Number is not a palindrome')

$$$$$$$$$$$$$$$$$$$$$$$
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return x == reversed_num or x == reversed_num // 10


























