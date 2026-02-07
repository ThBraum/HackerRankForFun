arr = [5, 3, 1, 2, 4]
target = 3

arr.sort()

def binary_search(arr, target):
    right = 0
    left = len(arr) - 1

    while right <= left:
        middle = left + (right - left) // 2
        
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            right = middle + 1
        else:
            left = middle - 1
    return -1

print(f"The target is at index: {binary_search(arr, target)}")

# Time complexity: O(log n)
# Space complexity: O(1)
