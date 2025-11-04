## **Bài 3.1: Tìm kiếm (Searching)**

### 1. Tìm kiếm tuyến tính (Linear Search)

* Duyệt từng phần tử của danh sách để tìm giá trị.
* **Đơn giản**, nhưng chậm với danh sách dài: `O(n)`.

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [4, 2, 7, 1]
print(linear_search(arr, 7))  # Output: 2
```

**Mermaid minh họa Linear Search**

```mermaid
graph LR
    A[Start] --> B[Check arr[0]]
    B -->|Not 7| C[Check arr[1]]
    C -->|Not 7| D[Check arr[2]]
    D -->|Found 7| E[Return index 2]
```

---

### 2. Tìm kiếm nhị phân (Binary Search)

* Áp dụng cho **danh sách đã sắp xếp**.
* Chia danh sách làm đôi, so sánh với giá trị giữa, loại nửa không cần tìm.
* **Độ phức tạp:** `O(log n)`.

```python
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 4, 7]
print(binary_search(arr, 4))  # Output: 2
```

**Mermaid minh họa Binary Search**

```mermaid
graph LR
    A[Start: arr=[1,2,4,7]] --> B[Check middle arr[1]=2]
    B -->|4>2| C[Search right half arr[2:3]]
    C --> D[Check middle arr[2]=4]
    D -->|Found| E[Return index 2]
```

---

### **Bài tập tìm kiếm**

1. Tìm số 11 trong danh sách `[1,3,5,7,9,11]` bằng linear search và binary search.
2. Viết hàm kiểm tra xem giá trị có tồn tại trong danh sách đã sắp xếp không bằng binary search.
3. So sánh số lần so sánh giữa linear search và binary search cho danh sách 10 phần tử.

