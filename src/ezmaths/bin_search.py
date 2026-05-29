def bin_search(array: list[int], obj: int) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == obj:
            return mid
        elif obj > array[mid]:
            left = mid + 1
        else:
            right = right + 1
    return -1