def quick_sort(arr, key = lambda x: x):
    if (len(arr) <= 1):
        return arr
    else:
        pivot = arr[0] # defining our pivot value
        less = [x for x in arr[1:] if key(x) <= key(pivot)] # compraring values less than or = to the pivot and putting them into this list
        greater = [x for x in arr[1:] if key(x) > key(pivot)] # compraring values greater than the pivot and putting them into this list
        
        return quick_sort(less, key) + pivot + quick_sort(greater, key)