1 ]n = 4
for i in range(1, n + 1):
    print(' '.join(str(j) for j in range(1, i + 1)))
------------------------------------------------------
1. n = 4 #We define the total number of rows we want in the pattern
#  required pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4

2. for i in range(1, n + 1):   This loop runs from 1 to 4 (since n + 1 = 5).
On each iteration, i represents the current row number.Loop iteration	Value of i	Output row


3. ' '.join(str(j) for j in range(1, i + 1)) # This part is very important — it creates one line of numbers like "1 2 3".
range(1, i + 1) → generates numbers from 1 to i.
str(j) → converts each number to string (since join() works with strings).
' '.join(...) → joins all strings with a space ' ' between them.
ex:
' '.join(str(j) for j in range(1, 2))	"1"
' '.join(str(j) for j in range(1, 3))	"1 2"
' '.join(str(j) for j in range(1, 4))	"1 2 3"
' '.join(str(j) for j in range(1, 5))	"1 2 3 4"

--------------------------------------------------
1.1] siiler can be achives with following code also ;/
n = 4
for i in range(1, n + 1):           # Outer loop → rows
    for j in range(1, i + 1):       # Inner loop → numbers in each row
        print(j, end=" ")           # Print numbers in the same line
    print()                         # Move to the next line after each row

2] requiured pattern:
1
2 2
3 3 3
4 4 4 4
logic:
    for i in range(1,5):
    print(' '.join(str(i)* i)) 


3]   1
     2 3
     4 5 6
     7 8 9 10

3.1] n = 4
     num = 1
     for i in range(1, n + 1):
         for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
         print() 
3.2 ] 
n = 5
num = 1
for i in range(1, n + 1):
    row = [str(num + j) for j in range(i)]
    print(' '.join(row))
    num += i
4 ] 
required 
1 2 3 4 
1 2 3 
1 2 
1  
i]num = 6
for i in range(1,num +1):
    for j in range( 1 , num -i ):
        print(j, end =' ')
        
    print()

ii]n = 4
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
iii]
n = 4
for i in range(n, 0, -1):
    print(' '.join(str(j) for j in range(1, i + 1)))

