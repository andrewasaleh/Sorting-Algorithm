import random # Used to randomly generate arrays
import matplotlib.pyplot as plt # For the graph
from matplotlib.widgets import Slider, Button # Needed for buttons, sliders etc.
from merge_sort import merge_sort # Importing merge algo file
from bubble_sort import bubble_sort # Importing bubble algo file
from quick_sort import quick_sort # Importing quick sort algo file
import numpy as np  # Needed for creating a range of colors
import time

is_paused = False # Control the pause state
sorting_time = 0  # Time in milliseconds

sorting_times = []
algorithms = []

# Sets up the window title to allow for renaming
def set_window_title(title):
    backend = plt.get_backend()
    figManager = plt.get_current_fig_manager()
    if backend == 'TkAgg':
        figManager.window.title(title)
    elif backend == 'wxAgg':
        figManager.window.SetTitle(title)
    elif backend in ['Qt4Agg', 'Qt5Agg']:
        figManager.window.setWindowTitle(title)
    elif backend == 'GTK3Agg':
        figManager.window.set_title(title)
    else:
        print(f"{backend}, your window is broken or not reflecting what you named it")

def update_leaderboard(): # This function adds a "leaderboard" to list off the names and times of the algorithms
    leaderboard_text = 'Algorithms'.ljust(20) + 'Times (ms)\n\n'
    for algo, time in zip(algorithms[::-1], sorting_times[::-1]):  # Reverse order to display latest first
        leaderboard_text += f'{algo:<40}{time:>10.2f}\n'
    ax.text(0.5, -0.25, leaderboard_text, color='black', ha='center', va='center', fontsize=10, transform=ax.transAxes)

def generate_array(array_size):
    global color_map  # Declare color_map as global to store the mapping for the array values (bars)
    array = [random.randint(0, 500) for _ in range(array_size)] # Array size so the x-axis range
    unique_values = sorted(set(array))  # Get unique values to assign unique colors
    # Generate colors for each unique value 
    colors = plt.cm.viridis(np.linspace(0, 1, len(unique_values)))
    color_map = {value: colors[i] for i, value in enumerate(unique_values)}
    return array

def plot_array(ax, values):
    ax.clear()
    colors = [color_map[value] for value in values]
    ax.bar(range(len(values)), values, color=colors)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    # Include sorting time in the title
    ax.set_title(f'Algorithm Sorter - Last Sort Time: {sorting_time:.2f} ms')
    update_leaderboard() # updates the leaderboard with the current times
    fig.canvas.draw_idle()

def perform_sort(event):
    global random_array
    # Example sort logic, replace with actual sorting call
    for step in range(len(random_array)):
        check_pause()  # Check if paused before each step
        # Sorting step simulation
        random_array[step] = random_array[step]  # Placeholder for actual sorting logic
        plot_array(ax, random_array)
        plt.pause(0.1)  # Pause to visualize each step
        
def update(val):
    global random_array  # Make sure we update the global reference
    array_size = int(slider.val)
    random_array = generate_array(array_size)
    if sort_algorithm is not None:
        sorted_array = sort_algorithm(random_array)
    else:
        sorted_array = random_array
    plot_array(ax, sorted_array)

def reset(event):
    global random_array, color_map  # Also reset the color map
    array_size = int(slider.val)
    random_array = generate_array(array_size)  # This will also regenerate color_map
    plot_array(ax, random_array)


def toggle_pause(event):
    global is_paused
    is_paused = not is_paused  # Toggle the pause state
    print("Pause state toggled:", is_paused)  # Optional: print statement to verify functionality

def check_pause():
    while is_paused:
        plt.pause(0.1)  # Use plt.pause to keep the GUI responsive

# Sorting algorithms function calls and explanations

def perform_merge_sort(event):
    """
    This function performs a merge sort on the global array 'random_array'.
    It records the start time, sorts the array using the 'merge_sort' function,
    records the end time, calculates the sorting time in milliseconds,
    and prints the sorting time to the console.
    """
    global random_array, sorting_time  # Use the global array and sorting_time
    
    if random_array is not None:
        start_time = time.time()  # Record start time
        
        for step in merge_sort(random_array):  # Sort the existing array
            check_pause()  # Check if the process should pause
            plot_array(ax, step)
            plt.pause(0.1)  # Pause to visualize each step
        
        sorting_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        sorting_times.append(sorting_time)
        algorithms.append("Merge Sort")

def perform_bubble_sort(event):
    """
    This function performs a bubble sort on the global array 'random_array'.
    It records the start time, sorts the array using the 'bubble_sort' function,
    records the end time, calculates the sorting time in milliseconds,
    and prints the sorting time to the console.
    """
    global random_array, sorting_time  # Use the global array
    
    if random_array is not None:
        start_time = time.time()  # Record start time
        
        for step in bubble_sort(random_array):  # Sort the existing array
            check_pause()  # Check if the process should pause
            plot_array(ax, step)
            plt.pause(0.1)  # Pause to visualize each step
        
        sorting_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        sorting_times.append(sorting_time)
        algorithms.append("Bubble Sort")

def perform_quick_sort(event):
    """
    This function performs a quick sort on the global array 'random_array'.
    It records the start time, sorts the array using the 'quick_sort' function,
    records the end time, calculates the sorting time in milliseconds,
    and prints the sorting time to the console.
    """
    global random_array, sorting_time  # Use the global array
    
    if random_array is not None:
        start_time = time.time()  # Record start time
        
        for step in quick_sort(random_array):  # Sort the existing array
            check_pause()  # Check if the process should pause
            plot_array(ax, step)
            plt.pause(0.1)  # Pause to visualize each step
        
        sorting_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        sorting_times.append(sorting_time)
        algorithms.append("Quick Sort")

##################################################################
##### Below is all the GUI code ##########################

if __name__ == "__main__":
    array_size = 10
    random_array = generate_array(array_size)
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)  # Adjust 'top' to provide space for buttons
    
    # Set the window title
    set_window_title("Pixel Pioneers GUI")

    # Allows for re-adjusting of the graph in the window based on margins
    plt.subplots_adjust(left=0.097, right=0.9, top=0.73, bottom=0.213)  # Increase top and bottom margins

    sort_algorithm = None  # No default sorting algorithm (user decides)
    
    plot_array(ax, random_array)  # Plotting the unsorted array initially as random and unsorted

    slider_ax = fig.add_axes([0.2, 0.85, 0.6, 0.03])  # Moved above
    slider = Slider(slider_ax, 'Array Size', 1, 50, valinit=array_size, valstep=1)
    slider.on_changed(update)
    
    # TOP ROW (above the index slider)
    # Merge sort button (Top row, left)
    merge_sort_button_ax = fig.add_axes([0.2, 0.92, 0.2, 0.05]) # [left, bottom, width, height]
    merge_sort_button = Button(merge_sort_button_ax, 'Merge Sort')
    merge_sort_button.on_clicked(perform_merge_sort)

    # Bubble sort button (Top row, middle)
    bubble_sort_button_ax = fig.add_axes([0.4, 0.92, 0.2, 0.05]) # [left, bottom, width, height]
    bubble_sort_button = Button(bubble_sort_button_ax, 'Bubble Sort')
    bubble_sort_button.on_clicked(perform_bubble_sort)

    # Quick sort button (Top row, right)
    quick_sort_button_ax = fig.add_axes([0.6, 0.92, 0.2, 0.05]) # [left, bottom, width, height]
    quick_sort_button = Button(quick_sort_button_ax, 'Quick Sort')
    quick_sort_button.on_clicked(perform_quick_sort)

    # BOTTOM ROW (below the index slider)
    # Pause button (bottom row, left)
    pause_button_ax = fig.add_axes([0.20, 0.78, 0.2, 0.05])  # [left, bottom, width, height]
    pause_button = Button(pause_button_ax, 'Pause/Resume')
    pause_button.on_clicked(toggle_pause)

    # Generate Array button (bottom row, middle)
    generate_array_button_ax = fig.add_axes([0.4, 0.78, 0.2, 0.05])  # [left, bottom, width, height]
    generate_array_button = Button(generate_array_button_ax, 'Generate Array')
    generate_array_button.on_clicked(update)

    # Reset button (bottom row, right)
    reset_button_ax = fig.add_axes([0.6, 0.78, 0.2, 0.05])  # [left, bottom, width, height]
    reset_button = Button(reset_button_ax, 'Reset')
    reset_button.on_clicked(reset)

    plt.show()