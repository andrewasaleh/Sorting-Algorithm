def quick_sort(arr, low=0, high=None):
    """
    This function implements the Quick Sort algorithm. It takes an array as input, along with optional low and high indices.
    The function uses a generator to yield the intermediate states of the array during the sorting process.
    """
    if high is None:
        high = len(arr) - 1
    # If the low index is less than the high index, we proceed with the sorting process.
    if low < high:
        # We call the partition function to find the pivot index.
        pivot_index = partition(arr, low, high)
        # We recursively call the quick_sort function on the left subarray.
        yield from quick_sort(arr, low, pivot_index - 1)
        # We recursively call the quick_sort function on the right subarray.
        yield from quick_sort(arr, pivot_index + 1, high)
        # We yield the final sorted array.
        yield arr

def partition(arr, low, high):
    """
    This function takes an array and two indices, low and high, as input. It rearranges the elements of the array such that all elements less than the pivot element come before it, and all elements greater than the pivot element come after it.
    The function returns the pivot index.
    """
    # We choose the last element as the pivot.
    pivot = arr[high]
    # We initialize a variable i to keep track of the index of the smaller element.
    i = low - 1
    # We iterate over the elements of the array between low and high (excluding high).
    for j in range(low, high):
        # If the current element is less than the pivot, we increment i and swap the elements at indices i and j.
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # We swap the pivot element with the element at index i + 1.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # We return the pivot index.
    return i + 1