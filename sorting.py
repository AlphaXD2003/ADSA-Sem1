import random
import math
array = []

def generate_random_number(starting = 0, ending = 10000):
    return random.randint(starting, ending)

def generate_random_array(number = 10000):
    global array
    for i in range(0,number):
        array.append(generate_random_number())

def print_array():
    global array
    length = len(array)
    for i in range(0, length):
        print(f"Array value at {i} index: {array[i]}")

def calculate_average(avg_arr = []):
    length = len(avg_arr)
    sum = 0
    for i in range(length):
        sum += avg_arr[i]
    return int(sum/length)

def swap_two_elements(array, index1, index2):
     if index1 < 0 or index1 >= len(array) or index2 < 0 or index2 >= len(array):
        print("Error: Index out of range")
        return
     array[index1] , array[index2] = array[index2] , array[index1]

def bubble_sort_implement(array=[]):
    iteration = 0
    swap = 0
    length = len(array)
    for i in range(0, length - 1):
        swapped = False
        for j in range(0, length - i - 1):
            iteration += 1
            if array[j] > array[j+1]:
                swap += 1
                swap_two_elements(array=array,index1=j, index2=j+1)
                swapped = True
        if not swapped:
            break
    return iteration, swap

def bubble_sort(array = []):
    print("********************")
    print("Which case do you want to see ?")
    print("Press 1 for Best Case.")
    print("Press 2 for Average Case.")
    print("Press 3 for Worst Case.")
    print("********************")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print('You choosed best case.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(run_count):
            iteration, swap = bubble_sort_implement(sorted(array.copy()))
            swap_array.append(swap)
            iteration_array.append(iteration)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array)})")
        print(f"Practical Best Case Time Complexity is: O({calculate_average(iteration_array)})")
        
    elif (choice == 2):
        print('You choosed best case.')
        new_array = array.copy()
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(run_count):
            iteration, swap = bubble_sort_implement(array=array.copy())
            swap_array.append(swap)
            iteration_array.append(iteration)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array) * len(new_array)})")
        print(f"Practical Best Case Time Complexity is: O({calculate_average(iteration_array)})")

    elif choice == 3:
        print('You choosed worst case.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(run_count):
            iteration, swap = bubble_sort_implement(sorted(array.copy(), reverse=True))
            swap_array.append(swap)
            iteration_array.append(iteration)
        
        print(f"Theorical Worst Case Time Complexity is: O({len(new_array) * len(new_array)})")
        print(iteration_array)
        print(f"Practical Worst Case Time Complexity is: O({calculate_average(iteration_array)})")
    else:
        print("Enter Valid Choice.")
        return
    
def selection_sort_implement(array=[]):
    length = len(array)
    swap = 0
    iteration = 0
    for i in range(0, length):
        min_index = i
        for j in range(i+1 , length):
            iteration+=1
            if(array[j] < array[min_index]):
                min_index = j
        swap+=1
        swap_two_elements(array=array,index1=i,index2=min_index)
    return iteration, swap

def selection_sort(array = []):
    print("********************")
    print("Which case do you want to see ?")
    print("Press 1 for Best Case.")
    print("Press 2 for Average Case.")
    print("Press 3 for Worst Case.")
    print("********************")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print('You choosed best case.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = selection_sort_implement(array=sorted(array.copy()))
            iteration_array.append(iteration)
            swap_array.append(swap)\
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array) * len(new_array)})")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: O({calculate_average(iteration_array)})")
    elif choice == 2:
        print('You choosed average case.')
        new_array = array.copy()
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = selection_sort_implement(array=array.copy())
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Average Case Time Complexity is: O({len(new_array) * len(new_array)})")
        print(iteration_array)
        print(f"Practical Average Case Time Complexity is: O({calculate_average(iteration_array)})")
    elif choice == 3:
        print('You choosed worst case.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = selection_sort_implement(sorted(array.copy(), reverse=True))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Average Case Time Complexity is: O({len(new_array) * len(new_array)})")
        print(iteration_array)
        print(f"Practical Average Case Time Complexity is: O({calculate_average(iteration_array)})")
    else:
        print("Please choose valid option.")
        return

def insertion_sort_implemenation(array = []):
    length = len(array)
    swap = 0
    iteration = 0
    for i in range (1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key :
            iteration += 1
            array[j+1] = array[j]
            j -= 1
        iteration += 1
        array[j+1] = key
        if j + 1 != i:
            swap += 1
    return iteration, swap

def insertion_sort(array=[]):
    print("********************")
    print("Which case do you want to see ?")
    print("Press 1 for Best Case.")
    print("Press 2 for Average Case.")
    print("Press 3 for Worst Case.")
    print("********************")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print('You choosed best case.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = insertion_sort_implemenation(array=sorted(array.copy()))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array) })")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: O({calculate_average(iteration_array)})")
    elif(choice == 2):
        print('You choosed average case.')
        new_array = array.copy()
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = insertion_sort_implemenation(array.copy())
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Average Case Time Complexity is: O({len(new_array) * len(new_array) })")
        print(iteration_array)
        print(f"Practical Average Case Time Complexity is: O({calculate_average(iteration_array)})")
    elif choice == 3:
        print('You choosed worst case.')
        new_array = array.copy()
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = insertion_sort_implemenation(array.copy())
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Worst Case Time Complexity is: O({len(new_array) * len(new_array) })")
        print(iteration_array)
        print(f"Practical Worst Case Time Complexity is: O({calculate_average(iteration_array)})")
    else:
        print("Please choose a valid option.")
        return

merge_iteration_count = 0
merge_swap_count = 0

def merge(array = [], left = 0,mid = (0+len(array) // 2), right = len(array)):
    global merge_iteration_count
    global merge_swap_count
    left_sub_array_size = mid - left + 1
    right_sub_array_size = right - mid
    left_sub_array = []
    right_sub_array = []

    for i in range (0, left_sub_array_size):
        left_sub_array.append(array[left + i])
    
    for i in range(0, right_sub_array_size):
        right_sub_array.append(array[mid+1+i])

    i = j = 0
    k = left
    

    while i < left_sub_array_size and j < right_sub_array_size:  
        merge_iteration_count += 1
        if left_sub_array[i] <= right_sub_array[j]:
            array[k] = left_sub_array[i]
            i += 1
            merge_swap_count
        else:
            array[k] = right_sub_array[j]
            j += 1
            merge_swap_count
        k += 1
    
    while i < left_sub_array_size:
        merge_iteration_count += 1
        merge_swap_count
        array[k] = left_sub_array[i]
        i += 1
        k += 1
    
    while j < right_sub_array_size:
        merge_iteration_count += 1
        merge_swap_count
        array[k] = right_sub_array[j]
        j += 1
        k += 1
    
    return merge_iteration_count, merge_swap_count

def merge_sort_main(array = [], low = 0, high = len(array)):
    if low >= high:
        return
    mid = (low+high)//2
    merge_sort_main(array, low, mid)
    merge_sort_main(array, mid+1, high)
    merge(array, low, mid, high)

def merge_sort_implemenation(array=[]):
    length = len(array)
    low = 0
    high = length - 1
    merge_sort_main(array=array,low=low,high=high)
    global merge_iteration_count
    global merge_swap_count
    iteration_count = merge_iteration_count
    swap_count = merge_swap_count
    merge_iteration_count = 0
    merge_swap_count = 0
    return iteration_count, swap_count

def merge_sort(array=[]):
    print("********************")
    print("Only Average case is Availiable.")
    print("Press 1 for input sorted data.")
    print("Press 2 for input revered sorted data.")
    print("Press 3 for input random data.")
    print("********************")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print('You choosed to input sorted data.')
        new_array = sorted(array.copy())
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = merge_sort_implemenation(array=sorted(array.copy()))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array)}log{len(new_array) } = {len(new_array) * math.log2(len(new_array))})")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: { calculate_average(iteration_array)}")
    elif choice == 2:
        print('You choosed to input reverse sorted data.')
        new_array = sorted(array.copy(), reverse=True)
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = merge_sort_implemenation(array=sorted(array.copy(), reverse= True))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array)}log{len(new_array) } = {len(new_array) * math.log2(len(new_array))})")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: { calculate_average(iteration_array)}")
    elif choice == 3:
        print('You choosed to input random  data.')
        new_array = array.copy()
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = merge_sort_implemenation(array=array.copy())
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array)}log{len(new_array) } = {len(new_array) * math.log2(len(new_array))})")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: { calculate_average(iteration_array)}")
    else:
        print("Please Choose Valid Option.")
        return 

quick_sort_iteration_count = 0
quick_sort_swap_count = 0


def generate_best_case_array(n):
    if n <= 0:
        return []
    
    # Create an array to store the best-case values for QuickSort
    best_case_array = [0] * n
    
    def fill_array(start, end, index):
        # Check if index is within array bounds
        if index >= n or start > end:
            return
        
        mid = (start + end) // 2
        best_case_array[index] = mid
        
        # Calculate left and right child indices
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Recursively fill left subtree
        if left_child < n:
            fill_array(start, mid - 1, left_child)
        
        # Recursively fill right subtree
        if right_child < n:
            fill_array(mid + 1, end, right_child)
    
    # Start filling the array
    fill_array(0, n - 1, 0)
    
    return best_case_array

def partition(array,low,high):
    global quick_sort_swap_count, quick_sort_iteration_count
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        quick_sort_iteration_count += 1
        if array[j] < pivot:
            i += 1
            quick_sort_swap_count += 1
            swap_two_elements(array=array,index1=i,index2=j)
    quick_sort_swap_count += 1
    swap_two_elements(array=array,index1=i+1,index2=high)
    return i+1

def quick_sort_main(array,low,high):
    if low  >= high :
        return
    pivot_index = partition(array=array,low=low,high=high)
    quick_sort_main(array,low,pivot_index-1)
    quick_sort_main(array,pivot_index+1,high)
    

def quick_sort_implementation(array = []):
    length = len(array)
    low = 0
    high = length - 1
    quick_sort_main(array,low,high)

    global quick_sort_swap_count, quick_sort_iteration_count
    iteration, swap =  quick_sort_swap_count, quick_sort_iteration_count
    quick_sort_swap_count = quick_sort_iteration_count = 0
    return iteration, swap

def quick_sort(array=[]):
    print("********************")
    print("Which case do you want to see ?")
    print("Press 1 for Best Case.")
    print("Press 2 for Average Case.")
    print("Press 3 for Worst Case.")
    print("********************")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        print('You choosed best case.')
        new_array = sorted(array.copy())
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            arr = generate_best_case_array(len(new_array))
            print(arr)
            iteration, swap = quick_sort_implementation(array=arr)
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array) }log{len(new_array)}) = {len(new_array) * math.log2(len(new_array))}")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: {calculate_average(iteration_array)}")
    elif(choice == 3):
        print('You choosed worst case.')
        n = 10000
        new_array = array.copy()[1:500]
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            # iteration, swap = quick_sort_implementation(array=(sorted(array.copy()))[1:500])
            iteration, swap = quick_sort_implementation(sorted(list(range(0,501))))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Worst Case Time Complexity is: O({len(new_array) }x {len(new_array)}) = {len(new_array) * len(new_array) }")
        print(iteration_array)
        print(f"Practical Worst Case Time Complexity is: {calculate_average(iteration_array)}")
    elif(choice == 2):
        print('You choosed worst case.')
        new_array = (array.copy())
        run_count = int(input("Enter the number of time You want to run this algorithm: "))
        swap_array = []
        iteration_array = []
        for i in range(0, run_count):
            iteration, swap = quick_sort_implementation(array=(array.copy()))
            iteration_array.append(iteration)
            swap_array.append(swap)
        
        print(f"Theorical Best Case Time Complexity is: O({len(new_array) }log{len(new_array)}) = {len(new_array) * math.log2(len(new_array))}")
        print(iteration_array)
        print(f"Practical Best Case Time Complexity is: {calculate_average(iteration_array)}")
    else :
        print("Choose Valid Option")
        return

def main_program():
    global array
    length = len(array)
    generate_random_array()

    while 1:
        print("*********Menu***********")
        print("Press 1 for Bubble Sorting")
        print("Press 2 for Selection Sorting")
        print("Press 3 to Insertion Sorting")
        print("Press 4 to Merge Sorting")
        print("Press 5 to Quick Sorting")
        print("Press 6 to Quit")
        print("************************")
        choice = int(input('Enter Your Choice: '))
        
        if choice == 1:
            print('You choosed Bubble Sort.')
            bubble_sort(array=array)           
        elif choice == 2:
            print('You choosed Selection Search.')
            selection_sort(array=array.copy())
            
        elif choice == 3:
            print('You choosed Insertion Sort.')
            insertion_sort(array=array.copy())
        elif choice == 4:
            print('You choosed Merge Sort.')
            merge_sort(array=array.copy())           
        elif choice == 5:
            print('You choosed Quick Search.')
            quick_sort(array=array.copy())           
        elif choice == 6:
            print('You choosed to Quit.')           
            break
        else :
            print('Enter Valid Choice to continue')
            continue

main_program()