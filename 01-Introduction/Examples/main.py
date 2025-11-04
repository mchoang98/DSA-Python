# Ví dụ phân tích độ phức tạp đơn giản
def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False
# độ phức tạp: O(n)
