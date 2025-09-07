"""
A Simple ATM Simulator

Start with a balance of $1000
Ask user what they want to do: check balance, deposit, or withdraw
For deposits: add amount to balance
For withdrawals: check if sufficient funds exist
Display appropriate messages and updated balance
"""
balance = 1000

while True:
    print("ATM Menu \nWhat do you want to do? \n1. Check balance \n2. Deposit \n3. Withdraw\n")
    action = int(input("Choose an option: "))

    if action == 1:
        print(f"Current balance = ${balance}\n")
        
    elif action == 2:
        print("How much do you want to deposit?")
        amount = int(input("Amount: "))
        balance = balance + amount

        print(f"Deposit Successfull! \nCurrent balance = ${balance}\n")

    elif action == 3:
        print("How much do you want to withdraw?")
        amount = int(input("Amount: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance - amount
            print(f"Withdrawal Successfull! \nCurrent balance = ${balance}\n")

    else:
        print("Action Unavailable.\n")
    


#    def deposit():
#     print("How much do you want to deposit?")
#     amount = int(input("Amount: "))
#     balance = balance + amount

#     print(f"Deposit Successfull! \nCurrent balance = ${balance}")

# def withdraw():
#     print("How much do you want to withdraw?")
#     amount = int(input("Amount: "))
#     if amount > balance:
#         print("Insufficient funds")
#     else:
#         balance = balance - amount
#         print(f"Withdrawal Successfull! \nCurrent balance = ${balance}")
    
# def checkBalance():
#     print(f"Current balance = ${balance}")