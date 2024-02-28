def merge_sort(arr, start=0, end=None):
    """
    This function implements the merge sort algorithm. It takes an array and two optional indices, start and end.
    If end is None, this is the first call to merge_sort.
    If the segment size is greater than 1, it needs sorting.
    """
    # If end is None, this is the first call to merge_sort
    if end is None:
        end = len(arr)
    # If the segment size is greater than 1, it needs sorting
    if end - start > 1:
        mid = (start + end) // 2  # Find the middle point to divide the array into two halves
        
        # Recursively sort the first half
        yield from merge_sort(arr, start, mid)
        # Recursively sort the second half
        yield from merge_sort(arr, mid, end)
        
        # Merge the sorted halves
        yield from merge(arr, start, mid, end)
        # Yield the entire array for visualization after each merge
        yield arr

def merge(arr, start, mid, end):
    """
    This function merges two sorted subarrays of arr[].
    The two subarrays are arr[start:mid] and arr[mid:end].
    """
    # Temporary arrays for left and right halves
    left = arr[start:mid]
    right = arr[mid:end]
    k = start  # Initial index of merged subarray
    i = j = 0  # Initial indexes of first and second halves
    
    # Merge the temp arrays back into arr[start:end]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        yield arr  # Yield for visualization after each insertion
        
    # Copy the remaining elements of left[], if there are any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr  # Yield for visualization after each insertion
       
    # Copy the remaining elements of right[], if there are any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr  # Yield for visualization after each insertion