weights = []
profit = []
items_index = []
item_inserted = []
item_count = 0
max_capacity = 0
total_weight = 0
total_profit = 0
def greedy_01knapsack():
    global weights, profit, item_count, max_capacity, total_weight, profit, items_index, item_inserted,total_profit
    
    max_capacity = int(input("Enter the maximum capacity of Knapsack: "))
    item_count = int(input("Enter the number of items: "))
    if item_count <= 0:
        return print('Please enter a valid item count greater than zero and try again.')
    for i in range(item_count):
        weights.append(int(input(f'Enter the weight of the {i+1}th itme: ')))
        profit.append(int(input(f'Enter the profit of the {i+1}th itme: ')))
        items_index.append(i)
    
    profitperweight = []
    items = []
    for i in range(item_count):
        profitperweight.append(profit[i]/weights[i])
        items.append((profit[i]/weights[i], profit[i], weights[i],items_index[i]))
    
    items.sort(reverse=True, key=lambda x: x[0])
    profitperweight = [item[0] for item in items]
    sorted_weights = [item[2] for item in items]
    sorted_profits = [item[1] for item in items]
    sorted_item_index = [item[3] for item in items]
    print(sorted_item_index)

    i = 0
    while total_weight < max_capacity and i < item_count:
        if sorted_weights[i] + total_weight > max_capacity:
            print('Maximum Capacity reached')
            break
        item_inserted.append(sorted_item_index[i])
        total_weight += sorted_weights[i]
        total_profit += sorted_profits[i]
        i += 1
    
    print(total_profit)
    print(item_inserted)

    print(f'Total profit accumulated: {total_profit}')
    print(f'Total weight of the Knapsack: {total_profit}')

    for i in range(len(item_inserted)):
        print(f'{item_inserted[i] + 1}th item is picked up that accumulated {profit[item_inserted[i]]} units profit and adds {weights[item_inserted[i]]} units weight.')
    
    
    


def dp_01knapsack():
    pass
def _01knapsack():
    print('***********************')
    print("Enter 1 for using Greedy Approach.")
    print("Enter 2 for using Dyanamic Programming.")
    print('***********************')
    choice = int(input("Enter Your choice: "))
    
    if choice == 1:
        greedy_01knapsack()
    elif choice == 2:
        dp_01knapsack()
    else :
        print('Enter a Valid Choice.')
        return
    

def fractional_knapsack():
    pass

def main_program():
    while 1:
        print("*********Menu***********")
        print("Press 1 for 0/1 Knapsack")
        print("Press 2 for Fractional Knapsack.")
        print("Press 3 to Quit")
        print("************************")
        choice = int(input('Enter Your Choice: '))

        if choice == 1:
            _01knapsack()
        elif choice == 2:
            fractional_knapsack()
        elif choice == 3:
            print("You choosed to Quit.")
            break
        else :
            print('Enter a Valid Choice.')
            continue

main_program()