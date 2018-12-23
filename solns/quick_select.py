#average run time O(n)
#worst case O(n^2)
#buggy, but vague familiarity 

def partition(arr, left, right):
    print(arr, left, right, arr[right])
    pivot = arr[right]
    i = left
    for j in range(right):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    print(arr)
    return i

def quickselect(arr, left, right, k):
    pivot = partition(arr, left, right)
    if k > 0 and k <= right - left + 1:
        if pivot - left == k - 1:
            return arr[k]
        elif pivot - left > k - 1:
            return quickselect(arr, left, pivot - 1, k)
        else:
            return quickselect(arr, pivot + 1, right, k - pivot + left - 1)
    raise Exception

def kth_smallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k)

print(kth_smallest([2, 1, 9, 3, 4], 1))