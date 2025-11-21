1]list():
*Mutable, ordered, allows duplicates
*Methods: append(), extend(), insert(), remove(), pop(), clear(), count(), index(), sort(), reverse(), copy()

Application: Dynamic data like task lists, queues, etc.
| **Method**  | **Example**             | **Application / Description**        |
| ----------- | ----------------------- | ------------------------------------ |
| `append()`  | `nums.append(10)`       | Add single element at the end.       |
| `extend()`  | `nums.extend([20, 30])` | Add multiple elements.               |
| `insert()`  | `nums.insert(1, 15)`    | Insert element at specific position. |
| `remove()`  | `nums.remove(15)`       | Remove first matching element.       |
| `pop()`     | `nums.pop()`            | Remove and return last element.      |
| `clear()`   | `nums.clear()`          | Remove all elements.                 |
| `index()`   | `nums.index(10)`        | Return index of first occurrence.    |
| `count()`   | `nums.count(10)`        | Count how many times value appears.  |
| `sort()`    | `nums.sort()`           | Sort list in ascending order.        |
| `reverse()` | `nums.reverse()`        | Reverse the list.                    |
| `copy()`    | `b = nums.copy()`       | Make a shallow copy of list.         |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2]tuple() / 10,  :
*Immutable, ordered, allows duplicates
*Methods: count(), index()

Application: Fixed data (e.g., coordinates, config values).
| **Method** | **Example**  | **Application / Description**                |
| ---------- | ------------ | -------------------------------------------- |
| `count()`  | `t.count(5)` | Count how many times value appears in tuple. |
| `index()`  | `t.index(5)` | Return index of first occurrence.            |



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  3] set():

*Mutable, unordered, unique elements
*Methods: add(), remove(), discard(), pop(), clear(), update()
*Application: Membership testing, removing duplicates, set operations.
  
| **Method**               | **Example**                 | **Application / Description**                       |
| ------------------------ | --------------------------- | --------------------------------------------------- |
| `add()`                  | `s.add(10)`                 | Add single element to set.                          |
| `remove()`               | `s.remove(5)`               | Remove specific element (error if not found).       |
| `discard()`              | `s.discard(5)`              | Remove element if present, no error if missing.     |
| `pop()`                  | `s.pop()`                   | Remove and return random element.                   |
| `clear()`                | `s.clear()`                 | Remove all elements from set.                       |
| `update()`               | `s.update([4,5,6])`         | Add multiple elements.                              |
| `copy()`                 | `b = s.copy()`              | Make a shallow copy of set.                         |
| `union()`                | `s.union(t)`                | Return new set with all elements from both.         |
| `intersection()`         | `s.intersection(t)`         | Return common elements.                             |
| `difference()`           | `s.difference(t)`           | Return elements in `s` but not in `t`.              |
| `symmetric_difference()` | `s.symmetric_difference(t)` | Return elements in either `s` or `t`, but not both. |


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4]dict(): 

*Key–value pairs, mutable
*Methods: get(), keys(), values(), items(), update(), pop(), clear(), setdefault(), fromkeys()
*Application: Fast lookups (like storing user data, word counts, etc.)

                           
| **Method**     | **Example**                     | **Application / Description**                       |
| -------------- | ------------------------------- | --------------------------------------------------- |
| `get()`        | `d.get('name', 'Unknown')`      | Return value for key or default if not found.       |
| `keys()`       | `d.keys()`                      | Return all keys.                                    |
| `values()`     | `d.values()`                    | Return all values.                                  |
| `items()`      | `d.items()`                     | Return key-value pairs as tuples.                   |
| `update()`     | `d.update({'age': 25})`         | Add or modify key-value pairs.                      |
| `pop()`        | `d.pop('age')`                  | Remove item with given key.                         |
| `clear()`      | `d.clear()`                     | Remove all items.                                   |
| `copy()`       | `new = d.copy()`                | Return shallow copy of dictionary.                  |
| `setdefault()` | `d.setdefault('city', 'Delhi')` | Return value if key exists, else add with default.  |
| `fromkeys()`   | `dict.fromkeys(['a','b'], 0)`   | Create new dictionary from keys with default value. |


OVERVIEW:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

| Method / Operation | **List** |      **Tuple**     |             **Set**             |    **Dictionary**    |
| ------------------ | :------: | :----------------: | :-----------------------------: | :------------------: |
| `append()`         |   ✅ Yes  |        ❌ No        |               ❌ No              |         ❌ No         |
| `extend()`         |   ✅ Yes  |        ❌ No        |               ❌ No              |         ❌ No         |
| `insert()`         |   ✅ Yes  |        ❌ No        |               ❌ No              |         ❌ No         |
| `remove()`         |   ✅ Yes  |        ❌ No        | ✅ Yes (`discard()` alternative) |         ❌ No         |
| `pop()`            |   ✅ Yes  |        ❌ No        |   ✅ Yes (removes random item)   |    ✅ Yes (by key)    |
| `clear()`          |   ✅ Yes  |        ❌ No        |              ✅ Yes              |         ✅ Yes        |
| `index()`          |   ✅ Yes  |        ✅ Yes       |               ❌ No              |         ❌ No         |
| `count()`          |   ✅ Yes  |        ✅ Yes       |               ❌ No              |         ❌ No         |
| `sort()`           |   ✅ Yes  |        ❌ No        |               ❌ No              |         ❌ No         |
| `reverse()`        |   ✅ Yes  |        ❌ No        |               ❌ No              |         ❌ No         |
| `copy()`           |   ✅ Yes  | ❌ No (use slicing) |              ✅ Yes              |         ✅ Yes        |
| `update()`         |   ❌ No   |        ❌ No        |              ✅ Yes              |         ✅ Yes        |
| `get()`            |   ❌ No   |        ❌ No        |               ❌ No              |         ✅ Yes        |
| `keys()`           |   ❌ No   |        ❌ No        |               ❌ No              |         ✅ Yes        |
| `values()`         |   ❌ No   |        ❌ No        |               ❌ No              |         ✅ Yes        |
| `items()`          |   ❌ No   |        ❌ No        |               ❌ No              |         ✅ Yes        |
| `setdefault()`     |   ❌ No   |        ❌ No        |               ❌ No              |         ✅ Yes        |
| `fromkeys()`       |   ❌ No   |        ❌ No        |               ❌ No              | ✅ Yes (class method) |

imp
  

  | Feature / Aspect                           | **Assignment Operator (`=`)**                                                      | **`setdefault()`**                                                          | **`update()`**                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Purpose**                                | Add a new key or overwrite an existing key with a given value.                     | Return the value if key exists; otherwise add the key with a default value. | Add or modify multiple key–value pairs at once (from another dict or iterable). |
| **Usage Syntax**                           | `dict[key] = value`                                                                | `dict.setdefault(key, default)`                                             | `dict.update(other_dict)` or `dict.update(key=value)`                           |
| **If key exists**                          | Value is **overwritten**.                                                          | Existing value is **returned** (no overwrite).                              | Value is **overwritten**.                                                       |
| **If key does not exist**                  | Adds key with the given value.                                                     | Adds key with the default value and returns it.                             | Adds new key–value pairs.                                                       |
| **Return value**                           | Returns the **assigned value** when accessed later. (No return during assignment.) | Returns the **value** of the key (existing or new).                         | Returns **None** (modifies in place).                                           |
| **Number of keys handled**                 | One key at a time.                                                                 | One key at a time.                                                          | Multiple keys at once.                                                          |
| **Modifies dictionary?**                   | ✅ Yes                                                                              | ✅ Yes (only if key doesn’t exist)                                           | ✅ Yes                                                                           |
| **Overwrites data?**                       | ✅ Yes                                                                              | ❌ No                                                                        | ✅ Yes                                                                           |
| **Supports iterables / multiple updates?** | ❌ No                                                                               | ❌ No                                                                        | ✅ Yes (dict, list of tuples, kwargs)                                            |
| **Raises KeyError?**                       | ❌ No (creates new key)                                                             | ❌ No                                                                        | ❌ No                                                                            |
| **Common use-case**                        | Direct assignment / updating values.                                               | Setting default values (like initializing missing data).                    | Merging or bulk-updating dictionaries.                                          |


  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
a]  setdefault() :
# Setting default marks for students
marks = {}
for name in ['Amit', 'Ravi', 'Amit']:
    marks.setdefault(name, 0)
    marks[name] += 10
print(marks)#{'Amit': 20, 'Ravi': 10}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

b]swapcase() — String Method 
works with string and string part of sequencial data types .
swapcase() is a built-in string method that toggles the case of each letter:
Uppercase → Lowercase
Lowercase → Uppercase

text = "HeLLo123"
print(text.swapcase())
output: hEllO123

b.1]mannual method
l1 = ['a', 'A', 'c', 'G']
l2 = []

for i in l1:
    if 'A' <= i <= 'Z':          # if uppercase
        l2.append(chr(ord(i) + 32))   # convert to lowercase
    elif 'a' <= i <= 'z':        # if lowercase
        l2.append(chr(ord(i) - 32))   # convert to uppercase

print(l2)

