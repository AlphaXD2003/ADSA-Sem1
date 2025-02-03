
def greedy():
    return print("Not Solvavble using Greedy.")

def dp_approach():
    string1 = input("Enter the first string: ")
    length1 = len(string1)
    string2 = input("Enter the first string: ")
    length2 = len(string2)

    dp = [[0] * (length2+1) for _ in range (length1+1)]

    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    
    # calculate
    lcs_str = ""
    i,j = length1,length2
    while i >0 and j > 0:
        if string1[i-1] == string2[j-1]:
            lcs_str = string1[i-1] + lcs_str
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    
    print(f"Longest Common subsequence between {string1} and {string2} is: {lcs_str}")
    return

def main_program():
    
    while True:
        print('********Menu Opens********')
        print("Enter 1 for choosing Dynamic Programming approach to solve LCS.")
        print("Enter 2 for choosing Greedy approach to solve LCS.")
        print("Enter 3 to Quit.")
        print('********Menu Closes********')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            dp_approach()
        elif choice == 2:
            greedy()
        elif choice == 3:
            break
        else:
            print("Enter a valid option.")
            continue

main_program()