def bubble_sort(arr):
    """
    This function implements the bubble sort algorithm.
    
    Parameters:
    arr (list): A list of integers to be sorted.
    
    Returns:
    None: The function does not return any value. Instead, it yields a copy of the sorted array at each step of the sorting process.
    
    Yields:
    list: A copy of the sorted array at each step of the sorting process.
    
    Example:
    >>> bubble_sort([3, 2, 1])
    [2, 3, 1]
    [1, 2, 3]
    """
    
    # Get the length of the array
    n = len(arr)
    
    # Iterate through the array
    for i in range(0, n):
        
        # Inner loop to compare adjacent elements and swap them if necessary
        for j in range(0, n - i - 1): # syntax to implement the j-i-2 part in the pseudo-code
            
            # If the current element is greater than the next element
            if (arr[j] > arr[j+1]):
                
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Yield a copy of the sorted array at this step
                yield arr.copy()  # Yield a copy to ensure the state is captured at this moment