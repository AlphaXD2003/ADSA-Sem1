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

def linear_search(array = []):
    length = len(array)
    print(f"The length of the array is {length}.")
    run_count = int(input('Specify the number of times you want to run the algo: '))
    complexity_array = []
    for i in range(0, run_count):
        print("Possbile values present in the array lie between 0 to 10,000.")
        search_number = int(input("Enter the number you want to search: "))
        flag = 0
        for i in range(length):
            if(array[i] == search_number):
                flag+=1
                print(f"The value is present at the index of {i}")
                complexity_array.append(i)
                break
        
        if(flag == 0):
            print("The value is not present.")
            complexity_array.append(length - 1)
    
    print(f"Theoritical Time Complexity : O({length})")
    print(f"Practical Time Complexity : O({calculate_average(complexity_array)})")

count_for_binary_search = 0

def binary_search_implement(array, low, high, number ):
    global count_for_binary_search
    mid = (low+high) // 2
    count_for_binary_search +=1
    if(low > high):
        return -1, count_for_binary_search
    if(array[mid] == number):
        print(f"The value is present in the array at the index of {mid}")
        return mid, count_for_binary_search
    elif number < array[mid]:
        return binary_search_implement(array, low=low, high=mid-1,number=number)
    else:
        return binary_search_implement(array, low=mid+1, high=high,number=number)

def binary_search(array = []):
    global count_for_binary_search
    length = len(array)
    low = 0
    high = length - 1
    print(f"The length of the array is {length}.")
    run_count = int(input('Specify the number of times you want to run the algo: '))
    complexity_array = []
    for i in range (run_count):
        print("Possbile values present in the array lie between 0 to 10,000.")
        search_number = int(input("Enter the number you want to search: "))
        count_for_binary_search = 0
        index , count = binary_search_implement(array=array, low=low, high=high, number=search_number)
        if(index == -1):
            print("The value is not present")
        else:
            print(f"The value is present at {index}")
        complexity_array.append(count)

    print(f"Theoritical Time Complexity : O(log {length}) = {math.log2(length)}")
    print(f"Practical Time Complexity : {calculate_average(complexity_array)}")
    

def main_program():
    global array
    length = len(array)
    generate_random_array()
    
    while 1:
        print("*********Menu***********")
        print("Press 1 for Linear Search")
        print("Press 2 for Binary Search")
        print("Press 3 to Quit")
        print("************************")
        choice = int(input('Enter Your Choice: '))
        
        if choice == 1:
            print('You choosed Linear Search.')
            linear_search(array=array)
            
        elif choice == 2:
            print('You choosed Binary Search.')
            binary_search(array=sorted(array.copy()))
            
        elif choice == 3:
            print('You choosed to quit.')
            break
        else :
            print('Enter Valid Choice to continue')
            continue
            
main_program()