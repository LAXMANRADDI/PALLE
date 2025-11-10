1]list():
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

2]tuple() / 10, 
| **Method** | **Example**  | **Application / Description**                |
| ---------- | ------------ | -------------------------------------------- |
| `count()`  | `t.count(5)` | Count how many times value appears in tuple. |
| `index()`  | `t.index(5)` | Return index of first occurrence.            |













































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
