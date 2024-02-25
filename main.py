import tkinter as tk # for the GUI
import pygame as pg # visualization
import time as time # to calculate execution time
import random # to generate the array of random numbers

def generate_array(): 
    print("Generate array button was pressed") # here we will generate a random array

def get_index_value(): # 
    value_label.config(text="Selected Value: {}".format(scale_var.get()))


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

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1): # syntax to implement the j-i-2 part in the psuedo- code
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr, key = lambda x: x):
    if (len(arr) <= 1):
        return arr
    else:
        pivot = arr[0] # defining our pivot value
        less = [x for x in arr[1:] if key(x) <= key(pivot)] # compraring values less than or = to the pivot and putting them into this list
        greater = [x for x in arr[1:] if key(x) > key(pivot)] # compraring values greater than the pivot and putting them into this list
        
        return quick_sort(less, key) + pivot + quick_sort(greater, key)



# below creates the main window
root = tk.Tk()
root.title("Pixel Pioneers Gui")

# Create variables to hold the state of the checkboxes
merge_sort_var = tk.BooleanVar()
bubble_sort_var = tk.BooleanVar()
quick_sort_var = tk.BooleanVar()

# Sorting algorithm checkboxes are below
merge_sort_checkbox = tk.Checkbutton(root, text="Merge Sort", variable=merge_sort_var)
merge_sort_checkbox.pack()

bubble_sort_checkbox = tk.Checkbutton(root, text="Bubble Sort", variable=bubble_sort_var)
bubble_sort_checkbox.pack()

quick_sort_checkbox = tk.Checkbutton(root, text="Quick Sort", variable=quick_sort_var)
quick_sort_checkbox.pack()
###############################################


# Create a scale widget
scale_var = tk.DoubleVar()
scale = tk.Scale(root, variable=scale_var, from_=0, to=100, orient="horizontal", length=300)
scale.pack(pady=20)

# Create a button to get the selected value
get_index_value_button = tk.Button(root, text="Set Index", command=get_index_value)
get_index_value_button.pack()

# Create a label to display the selected value
value_label = tk.Label(root, text="Index Value: {}".format(scale_var.get()))
value_label.pack()


# Creates the generate array button
generate_array_button = tk.Button(root, text = "Generate Array", command = generate_array)
generate_array_button.pack()



# Running the GUI
root.mainloop()