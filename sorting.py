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

def insertion_sort(array):
    pass

def merge_sort(array):
    pass

def quick_sort(array):
    pass



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
            print('You choosed Linear Search.')
            bubble_sort(array=array)           
        elif choice == 2:
            print('You choosed Binary Search.')
            selection_sort(array=sorted(array.copy()))
            
        elif choice == 3:
            print('You choosed Binary Search.')
            insertion_sort(array=sorted(array.copy()))
        elif choice == 4:
            print('You choosed Binary Search.')
            merge_sort(array=sorted(array.copy()))           
        elif choice == 5:
            print('You choosed Binary Search.')
            quick_sort(array=sorted(array.copy()))           
        elif choice == 6:
            print('You choosed to Quit.')           
            break
        else :
            print('Enter Valid Choice to continue')
            continue

main_program()