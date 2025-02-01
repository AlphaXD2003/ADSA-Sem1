weights = []
profit = []
items_index = []
item_inserted = []
item_count = 0
max_capacity = 0
total_weight = 0
total_profit = 0
referred = False
def greedy_01knapsack():
    global weights, profit, item_count, max_capacity, total_weight, profit, items_index, item_inserted,total_profit, referred
    
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
    
    
    print('Do you want to check for the optimal solution ?')
    print('Press 0 to deny.')
    print('Press 1 to accept.')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        referred = True
        dp_01knapsack()
    elif choice == 0:
        print('You denied to check the optimal solution.')
        print('Resetting data....')
        weights = []
        profit = []
        items_index = []
        item_inserted = []
        item_count = 0
        max_capacity = 0
        total_weight = 0
        total_profit = 0
        print('Data Reset successfully....')
    else:
        print('Please Enter valid choice. ')
        return
    
def dp_01knapsack():
    global weights, profit, item_count, max_capacity, total_weight, profit, items_index, item_inserted,total_profit, referred

    if not referred:
        max_capacity = int(input("Enter the maximum capacity of Knapsack: "))
        item_count = int(input("Enter the number of items: "))
        if item_count <= 0:
            return print('Please enter a valid item count greater than zero and try again.')
        for i in range(item_count):
            weights.append(int(input(f'Enter the weight of the {i+1}th itme: ')))
            profit.append(int(input(f'Enter the profit of the {i+1}th itme: ')))
            items_index.append(i)
     
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(item_count + 1)]
    
    for i in range(1, item_count+1):
        for j in range(1, max_capacity + 1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], profit[i-1] + dp[i-1][j-weights[i-1]])
    
    print(dp)
    
    optimal_profilt = dp[item_count][max_capacity]
    print(f"Maximum profit achievable by DP is: {optimal_profilt}")

    w = max_capacity
    selected_items = []

    for i in range(item_count, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item `i-1` was included
            selected_items.append(i - 1)
            w -= weights[i - 1]

    for item in selected_items:
        print(f"{item + 1}th item -> Profit: {profit[item]}, Weight: {weights[item]}")
    print(f"Total weight of the Knapsack in the optimal solution: {sum(weights[item] for item in selected_items)}")

    if referred:
        # Compare greedy and DP solutions
        print("\nComparison of Greedy and DP solutions:")
        print(f"Greedy Total Profit: {total_profit}")
        print(f"Greedy Total Weight: {total_weight}")
        print(f"Optimal Total Profit: {optimal_profilt}")
        print(f"Optimal Total Weight: {sum(weights[item] for item in selected_items)}")

    # Reset the `referred` flag and all data for a clean restart
    print("\nResetting data for fresh execution...")
    weights.clear()
    profit.clear()
    items_index.clear()
    item_inserted.clear()
    item_count = 0
    max_capacity = 0
    total_weight = 0
    total_profit = 0
    referred = False
    print("Data reset successfully.\n")

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
    global weights, profit, item_count, max_capacity, total_weight, profit, items_index, item_inserted,total_profit
    print("Greedy Approach gives both fast and optimal result for Fractional Knapsack.")
    max_capacity = int(input("Enter the maximum capacity of Knapsack: "))
    item_count = int(input("Enter the number of items: "))
    if item_count <= 0:
        return print('Please enter a valid item count greater than zero and try again.')
    for i in range(item_count):
        weights.append(int(input(f'Enter the weight of the {i+1}th itme: ')))
        profit.append(int(input(f'Enter the profit of the {i+1}th itme: ')))
        items_index.append(i)
    
    items = []
    for i in range(item_count):
        items.append([profit[i]/weights[i] , profit[i], weights[i], items_index[i]])
    
    items.sort(reverse=True, key=lambda x : x[0])
    sorted_weight = [item[2] for item in items]
    sorted_profit = [item[1] for item in items]
    sorted_item_index = [item[3] for item in items]
    sorted_profit_per_weight = [item[0] for item in items]

    i = 0
    k = max_capacity
    while total_weight < max_capacity and i < item_count:
        if k >= sorted_weight[i]:
            total_profit = total_profit + sorted_profit[i]
            k = k - sorted_weight[i]
            total_weight = total_weight + sorted_weight[i]
            print(f"Item {sorted_item_index[i] + 1} added {sorted_profit[i]} profit.")
        elif k > 0:
            total_profit = total_profit + (k * sorted_profit_per_weight[i])
            print(f"Item {sorted_item_index[i] + 1} added {k * sorted_profit_per_weight[i]} profit.")
            k = 0
            total_weight = max_capacity
            break
        i+=1
    print(f"Total Profit: {total_profit}")
    print(f"Total Weight: {total_weight}")
    

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