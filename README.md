# sorting-algorithm Visualization Application
This Python application visualizes different sorting algorithms using matplotlib. It allows users to interact with the visualization through a GUI, enabling them to see how bubble sort, merge sort, and quick sort algorithms sort an array of random integers in real time.

## Powerpoint Presentation 
https://adcsuf-my.sharepoint.com/:p:/g/personal/salehandrew110_csu_fullerton_edu/ETpRVHHKkxlBqO-qA8wu3hEBSHiGWuGfxrlagBUNLy_NMA?e=gzBCIH

## LinkedIn Video
https://www.linkedin.com/posts/joshuareyes0911_csuf-activity-7169233514175868928-yXnh?utm_source=share&utm_medium=member_desktop

## Features
- Visualization of bubble sort, merge sort, and quick sort algorithms.
- Interactive GUI with options to pause/resume sorting, generate new arrays, and adjust the array size.
- Sorting time measurement and display for each algorithm.
- Algorithm "leaderboard" displaying the execution times.
  
## Dependencies
To run this application, you need the following Python libraries:
- random for generating random arrays. (Standard Library)
- matplotlib for creating the GUI and visualizing the sorting process.
- numpy for generating a range of colors for the array elements.
- time for measuring the duration of each sorting algorithm's execution and to implement delays (pauses) in the visualization. (Standard Library)
- Additionally, you need the sorting algorithms (merge_sort, bubble_sort, quick_sort) available in your project directory.

## Setup and Installation
- Ensure Python is installed on your system.
- Install the required Python packages:
- Copy code
- pip install matplotlib numpy
- Place the sorting algorithm scripts (merge_sort.py, bubble_sort.py, quick_sort.py) in the same directory as this script.

## Controls
- Array Size Slider: Adjust the size of the array to be sorted.
- Sort Buttons: Choose the sorting algorithm to visualize.
- Pause/Resume Button: Pause or resume the sorting process.
- Generate Array Button: Generate a new array with random values.
- Reset Button: Reset the array to its initial unsorted state while it also captures and displays time recorded below the graph.

## Sorting Algorithms Explained
- Merge Sort
A divide-and-conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

- Bubble Sort
A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

- Quick Sort
An efficient divide-and-conquer algorithm that picks an element as pivot and partitions the given array around the picked pivot.

## Sorting Algorithms
- Each sorting algorithm (merge_sort, bubble_sort, quick_sort) visualizes the sorting process step by step. The algorithms record the sorting time and display it in the GUI.

## Leaderboard
The update_leaderboard function updates the GUI with a leaderboard showing the algorithms' names and their corresponding sorting times in milliseconds.

## Contributers
- Andrew Saleh
- Kevin Ramirez
- Alex Reyes
- Joshua Reyes

