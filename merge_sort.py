def merge_sort(arr): # arr is the name of the liss we are passing the the function
    if (len(arr) > 1): # Check if array has more than one element, if it does; it needs sorting
        mid = (len(arr) // 2)
        left_sublist = arr[:mid] # Creating left (1st half) sublist and assigning this to "left_side"
        right_sublist = arr[mid:] # Creating right (2nd half) sublist and assigning this to "right_side"

        merge_sort(left_sublist) # Recursively apply merge sort to the left sublist
        merge_sort(right_sublist) # Recursively apply merge sort to the right sublist

        i = j = k = 0 # assigning pointers == 0
    # i = the current index for the LEFT sublist
    # j = the current index for the RIGHT sublist
    # k = the current index for the MAIN array(list)

        while ((i < len(left_sublist)) and (j < len(right_sublist))): # continue the loop as long as there are elements in both sublists
            if (left_sublist[i] < right_sublist[j]): # checking if the current element in the left sublist is less than the current index of the right sublist
                arr[k] = left_sublist[i] # assign whatever value in the MAIN list to the value of the left sublist
                i += 1 # keep increasing the index value for the leftsublist
        
            else:
                arr[k] = right_sublist[j] # place the current element right sublist
                j += 1  # move the pointer in the right sublist
        
            k += 1 # reguardless where the value was taken from, we have to move to the next index slot for the MAIN list

        while (i < len(left_sublist)): # handles the scenario where 1 sublist is exhausted before the other
            arr[k] = left_sublist[i]
            i += 1
            k += 1

        while (j < len(right_sublist)): # handles the scenario where 1 sublist is exhausted before the other
            arr[k] = right_sublist[j]
            j += 1
            k += 1
    
    return arr
    # SUMMARY: Divide, Conquer, Combine