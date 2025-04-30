# Linear Search Algorithm

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [5, 10, 15, 20, 25]
target = 15

index = linear_search(numbers, target)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found.")

