import random
import math

amount = 0
coin_array = []
coin_supply_array = []
coins_inorder = []

def greedy_infinite():
    global amount, coin_array, coin_supply_array,coins_inorder
    amount = int(input("Enter the amount you want to achieve: "))
    print(amount)
    if amount <= 0:
        print("Amount must be greater than zero. Try again.")
        return
    while True:
        coin = int(input("Enter the coin you want to add. (Enter '0' to quit): "))
        if coin == 0:
            break
        if coin <= 0:
            print("Coin denomination must be positive.")
            continue
        coin_array.append(coin)
    if (len(coin_array) == 0):
        print("You didnot enter any coins. Try Again")
        return
    coin_array.sort(reverse=True)
    new_amount = amount + 0
    print(new_amount)
    for coin in coin_array:
        if new_amount == 0:
            break
        needed_coins = new_amount // coin  
        coins_inorder.extend([coin] * needed_coins)  # Add these coins to the result
        new_amount %= coin  


    print(f"Total Amount reachable: {amount - new_amount}")
    if new_amount > 0:
        print(f"Cannot fully reach the amount. Remaining amount: {new_amount}")
    else:
        print("Exact amount achieved!")
    coin = None
    for i in range(len(coins_inorder)):
        if coin == coins_inorder[i]:
            continue
        coin = coins_inorder[i]
        print(f"There are {coins_inorder.count(coin)} coins with weight {coin}")
        
    print('Already optimum as the coin supply is infinite.')
    amount = 0
    coin_array = []
    coins_inorder = []
    coin_supply_array = []

def greedy_finite():
    global amount, coin_array, coin_supply_array,coins_inorder
    amount = int(input("Enter the amount you want to achieve: "))
    if amount <= 0:
        print("Amount must be greater than zero. Try again.")
        return
    while True:
        coin = int(input("Enter the coin you want to add. (Enter '0' to quit): "))
        if coin == 0:
            break
        if coin <= 0:
            print("Coin denomination must be positive.")
            continue
        coin_array.append(coin)
    if (len(coin_array) == 0):
        print("You didnot enter any coins. Try Again")
        return
    
    for i in range(len(coin_array)):
        coin_supply_array.append(int(input(f"Enter the number of coins you want to allocate for {coin_array[i]}: ")))
    
    coin_supply_pairs = list(zip(coin_array, coin_supply_array)) 
    coin_supply_pairs.sort(reverse=True, key=lambda x: x[0])  

    coin_array, coin_supply_array = zip(*coin_supply_pairs) 

    coin_array = list(coin_array)
    coin_supply_array = list(coin_supply_array)

    new_amount = amount + 0
    coin_supply_array_dupl = coin_supply_array.copy()
    for i in range(len(coin_array)):
        coin = coin_array[i]
        required_coins = new_amount // coin
        total_coins = min(required_coins, coin_supply_array[i])
        new_amount %= (total_coins * coin)
        coin_supply_array_dupl[i] -= total_coins
        for j in range(total_coins):
            coins_inorder.append(coin)
    
    if new_amount > 0:
        print(f"Total amount reached is : {amount - new_amount}")
        print(f"Remaining amount  is : { new_amount}")
    
    c = None
    for coin in coins_inorder:
        if c == coin:
            continue
        print(f"The number of coins with weight {coin} is {coins_inorder.count(coin)}")
        c = coin
    
    for i in range (len(coin_supply_array_dupl)):
        print(f"Remianing coin(s) having weight {coin_array[i]} is {coin_supply_array_dupl[i]}")

    
    print("If You want to check whether it is optimum solution or not ?")
    print("Press 1 to check.")
    print("Press 2 to deny.")
    check = int(input("Enter your choice: "))
    if check == 1:
        greedy_approach()
    elif check == 2:
        print('You choosed not to check whether it is optimum or not.')
        print('Resetting all the data.........')
        amount = 0
        coin_array = []
        coin_supply_array = []
        coins_inorder = []
        print('Data is reset')
        return
    else:
        print("Enter valid choice")
        return

def greedy_approach():
    print("********************")
    print("Press 1 for having infinite supply of coins.")
    print("Press 2 for having limited numbers of coins.")
    print("********************")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        greedy_infinite()
    elif choice == 2:
        greedy_finite()
    else:
        print("Enter an valid choice and try again.")
        return

def dp_approach():
    pass

def main_program():
    while 1:
        print("*********Menu***********")
        print("Press 1 for using Greedy Approach")
        print("Press 2 for using Dynamic Programming")
        print("Press 3 to Quit")
        print("************************")
        choice = int(input('Enter Your Choice: '))

        if choice == 1:
            greedy_approach()
        elif choice == 2:
            dp_approach()
        elif choice == 3:
            print("You choosed to quit.")
            break
        else:
            print("Please choose an valid option.")
            continue

main_program()