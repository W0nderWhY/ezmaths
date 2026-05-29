from typing import Optional

def bin_search(array: list[int], obj: int, sorted:Optional[bool] = False) -> int:
    """Get object index in array

    Args:
        array: list filled with integers
        obj: integer, object in array
        sorted: bool, if array is already sorted set True, otherwise it will be sorted using Timsort and index will be in sorted array. By default is False
    
    Returns:
        Integer, index of element in array
    """
    def search():
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == obj:
                return mid
            elif obj > array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    if sorted:
        return search()
    else:
        array.sort()
        return search()