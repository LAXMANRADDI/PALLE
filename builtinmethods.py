














































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
