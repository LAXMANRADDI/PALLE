1) Reverse an array of 10 numbers using for loop
```python
arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")
```

---

2) Print numbers 1 to 100 in lines of 10 using for loop
num = 1
for i in range(1, 11):
    for j in range(10):
        print(num, end=" ")
        num += 1
    print()
```
**Output format:**
```
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
...
91 92 93 94 95 96 97 98 99 100
```
---
3) Count number of vowels in a string**
s = input("Enter string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print("Number of vowels:", count)
```
4) Calculate average of even numbers in an array of 10 numbers**
arr = [1,2,3,4,5,6,7,8,9,10]
sum_even = 0
count = 0

for i in arr:
    if i % 2 == 0:
        sum_even += i
        count += 1

if count != 0:
    avg = sum_even / count
    print("Average of even numbers:", avg)
else:
    print("No even numbers found")
```
