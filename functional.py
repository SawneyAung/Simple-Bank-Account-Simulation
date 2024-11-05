balance = 500
transactionHis = []  # Initialize transaction history

def deposit(amount):   
    global balance 
    balance += amount  # Add amount to balance
    print('')
    print(f'${amount} has been deposited to the account.')
    # Add the transaction to the transaction history
    transactionHistory('d', amount)

def withdraw(amount):
    global balance
    if amount > balance:  # Check if amount is greater than balance
        print('Insufficient Balance')
        return None
    else:
        balance -= amount  # Deduct amount from balance
        print('')
        print(f'${amount} has been withdrawn from the account.')
        # Add the transaction to the transaction history
        transactionHistory('w', amount)

def getBalance():
    print('')
    # Show account balance
    print(f'Your Account Balance: ${balance}')

def transactionHistory(option, amount):
    #checks if the transaction made was a deposit or a withdraw
    if option == 'd':
        transactionHis.append(f'Deposited ${amount}')
    elif option == 'w':
        transactionHis.append(f'Withdrawn ${amount}')

def menu():
    # Option menu for the user to choose from
    print('')
    print('Menu\n====')
    print('[1] Deposit')
    print('[2] Withdraw')
    print('[3] Show Balance')
    print('[4] Show Transaction History')
    print('[0] Exit')
    print('')
    option = int(input('Enter your option: '))  # Ask for input from the user
    return option  # Return the user's chosen option

while True:  # Allow the menu to stay until the exit option is chosen
    option = menu()
    if option == 0:  # If option 0 is chosen, exit the program
        print('')
        print('Exiting the program')
        break

    elif option == 1:  # If option 1 is chosen, use the deposit function
        print('')
        amount = int(input('Enter the amount: '))  # Ask for deposit amount
        confirm = input("Confirm?[y/n]: ")  # Ask for confirmation
        if confirm.lower() == 'y':
            deposit(amount)  # Deposit the amount
        else:
            print('Process has been cancelled')  # Cancel process if not confirmed
    
    elif option == 2:
        print('')
        amount = int(input('Enter the amount: '))  # Ask for withdrawal amount
        confirm = input('Confirm?[y/n]: ')  # Ask for confirmation
        if confirm.lower() == 'y':
            withdraw(amount)  # Withdraw the amount
        else:
            print('Process has been cancelled')  # Cancel process if not confirmed
        
    elif option == 3:
        # Show the account balance
        getBalance()

    elif option == 4:
        count = 0  # Record the number of transactions
        for transaction in transactionHis:
            count += 1  # Increment count for each transaction
            print('')
            print('Transaction History')
            print('')
            print(f'{count}. {transaction}')