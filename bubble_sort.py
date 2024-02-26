def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1): # syntax to implement the j-i-2 part in the psuedo- code
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr.copy()  # Yield a copy to ensure the state is captured at this moment
