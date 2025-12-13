ternanry condition for checking greatest of three numbres 
a ,b ,c =10 ,20,30
print (f'{a} is largest ' if a>b and a>c else(f'{b} is greater' if b>c  else f' {c} is largest ')) 
----------------------------------------------------------
   trenary with  help of tuples 

x = int ( input ('entr age: ') )
res = ('is not adult ' , 'is adult ')[x >= 18]
print (res)


--------------------------------------------------------------
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


* list cpmrehension practice:
1] Create a list of squares from 1 to 5:
squares = [x * x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

2]2. With Condition
Get all even numbers from 1 to 10: 
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10] 

3]  to capitalize each word in list :;
 Using Strings
Capitalize each word in a list:
words = ["python", "is", "fun"]
capitalized = [word.capitalize() for word in words]
print(capitalized)  # Output: ['Python', 'Is', 'Fun'] 


 4 ] 2d list ::
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in matrix for num in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5,6]


5] Find Common Elements (Set Intersection)
Given two lists, get the common elements 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]  # [3, 4] 

6] Filter and Transform
Given a list of integers, double only those which are divisible by 3:
nums = [1, 3, 4, 6, 7, 9]
result = [x * 2 for x in nums if x % 3 == 0] # [6, 12, 18]
