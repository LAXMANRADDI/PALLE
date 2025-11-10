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

2]tuple() / 10,  :
*Immutable, ordered, allows duplicates
*Methods: count(), index()

Application: Fixed data (e.g., coordinates, config values).
| **Method** | **Example**  | **Application / Description**                |
| ---------- | ------------ | -------------------------------------------- |
| `count()`  | `t.count(5)` | Count how many times value appears in tuple. |
| `index()`  | `t.index(5)` | Return index of first occurrence.            |




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
