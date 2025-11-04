# 2.1 Mảng & Chuỗi (Arrays & Strings)

## 1. Khái niệm

* **Mảng (Array)** là cấu trúc dữ liệu lưu trữ một **dãy phần tử liên tiếp** cùng kiểu dữ liệu.

  * Trong Python, **list** được dùng như mảng nhưng có thể chứa nhiều kiểu dữ liệu.
  * Ưu điểm: truy cập phần tử nhanh theo **chỉ số (index)**.
  * Nhược điểm: thêm/xóa ở giữa mảng tốn thời gian O(n).

* **Chuỗi (String)** là dãy ký tự.

  * Chuỗi trong Python là **immutable** (không thay đổi được trực tiếp).
  * Có thể truy cập, cắt (slice), nối (+), và thao tác với các hàm sẵn có.

---

## 2. Truy cập & Lưu trữ

### 2.1 Truy cập phần tử mảng

```python
arr = [10, 20, 30, 40, 50]
print(arr[0])    # 10
print(arr[3])    # 40
```

### 2.2 Truy cập phần tử chuỗi

```python
s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n' – phần tử cuối
```

### 2.3 Cập nhật mảng

```python
arr[2] = 35
print(arr)       # [10, 20, 35, 40, 50]
```

* **Lưu ý:** Chuỗi không thể thay đổi trực tiếp:

```python
# s[0] = 'J'  -> Lỗi!
s_new = 'J' + s[1:]
print(s_new)    # 'Jython'
```

---

## 3. Các thao tác phổ biến

### 3.1 Tìm phần tử lớn thứ hai

```python
arr = [10, 35, 20, 50, 40]
first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

print("Phần tử lớn thứ hai:", second)  # 40
```

---

### 3.2 Xoay mảng (rotate array)

Xoay phải 2 bước:

```python
arr = [1, 2, 3, 4, 5]
k = 2  # số bước xoay
n = len(arr)

rotated = arr[-k:] + arr[:-k]
print(rotated)   # [4,5,1,2,3]
```

---

### 3.3 Đảo chuỗi (reverse string)

```python
s = "Python"
reversed_s = s[::-1]
print(reversed_s)  # "nohtyP"
```

---

## 4. Ưu & Nhược điểm

| Cấu trúc  | Ưu điểm                                       | Nhược điểm                                                              |
| --------- | --------------------------------------------- | ----------------------------------------------------------------------- |
| Mảng/List | Truy cập nhanh theo index (O(1)), dễ thao tác | Thêm/xóa giữa mảng chậm (O(n)), kích thước cố định trong array thuần    |
| Chuỗi     | Dễ thao tác, hỗ trợ nhiều hàm sẵn có          | Không thay đổi trực tiếp (immutable), thao tác phức tạp cần tạo bản sao |

---

## 5. Bài tập luyện tập

1. **Tìm số lớn thứ hai**

* Viết hàm `second_largest(arr)` trả về phần tử lớn thứ hai của mảng.

2. **Xoay mảng**

* Viết hàm `rotate_array(arr, k)` xoay mảng `arr` sang phải `k` bước.

3. **Đảo chuỗi**

* Viết hàm `reverse_string(s)` đảo ngược chuỗi `s` mà không dùng slicing `[::-1]`.

4. **Đếm số ký tự**

* Cho một chuỗi, đếm số lần xuất hiện của từng ký tự.
* Gợi ý: dùng `collections.Counter`.

5. **Tìm phần tử duy nhất**

* Cho mảng chứa các số, chỉ có một số xuất hiện **một lần**, các số khác xuất hiện 2 lần.
* Viết hàm tìm phần tử duy nhất.
* Gợi ý: dùng XOR.

