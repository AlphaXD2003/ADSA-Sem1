import math
iteration = 0
def tower_of_hanoi(n, source, auxiliary, target):
    global iteration
    iteration+=1
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
def main_program():
    global iter
    count_of_disks = int(input("Enter the number of disks: "))
    print(f" -> For the count of {count_of_disks} the theritical iteration count is: (2^{count_of_disks} - 1) = {int(math.pow(2, count_of_disks) - 1)}")
    print("********Moves start from here********")
    tower_of_hanoi(count_of_disks, 'A', 'B', 'C')
    print("********Moves end here********")
    print(f"-> For the count of {count_of_disks} the practical iteration count is: {iteration}")

main_program()