import random
import time


class BankSystem:
    class Account:
        def __init__(self, account_number,name,balance=0.0):
            self.account_number = account_number
            self.name = name
            self.balance = balance

    def __init__(self):
        self.accounts = []
        self.total_accounts = 0

    def find_account(self, acc_no):
        for i in range(self.total_accounts):
            if self.accounts[i].account_number == acc_no:
                 return i
            return -1

    def generate_account_number(self):
        while True:
            acc_no = random.randint(10000000, 99999999)
            exists = False

            for acc in self.accounts:
                if acc.account_number == acc_no:
                    exists = True
                    break

            if not exists:
                return acc_no

    def create_account(self):
        if self.total_accounts >= 1000:
            print("Bank account storage full.")
            return
        name = input("Enter candidate name: ")
        new_acc_no = self.generate_account_number()

        new_account = self.Account(new_acc_no, name, 0.0)
        self.accounts.append(new_account)

        print("\nAccount created successfully!")
        print("Account Holder Name :", new_account.name)
        print("Account Number      :", new_account.account_number)
        print("Balance             : Rs.", new_account.balance)

        self.total_accounts += 1

    def view_account(self):
        acc_no = int(input("Enter account number: "))

        i = self.find_account(acc_no)
        if i == -1:
            print("Account not found.")
            return

        account = self.accounts[i]
        print("\n******** Account Details ********")
        print("Account Holder Name :", account.name)
        print("Account Number      :", account.account_number)
        print("Balance             : Rs.", account.balance)

    def deposit(self):
        acc_no = int(input("Enter account number: "))
        i = self.find_account(acc_no)


        if i == -1:
            print("Account not found.")
            return
        amount = float(input("Enter amount to deposit: "))


        if amount < 0:
            print("Invalid amount.")
            return

        self.accounts[i].balance += amount

        print(f"Rs. {amount} deposited successfully.")
        print("Update balance: Rs,",self.accounts[i].balance)

    def withdraw(self):

        acc_no = int(input("Enter account number: "))
        i = self.find_account(acc_no)
        if i == -1:
            print("Account not found.")
            return
        amount = float(input("Enter amount to withdraw:"))

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.accounts[i].balance:
            print("Insufficient balance.")
            return

        self.accounts[i].balance -= amount

        print(f"Rs. {amount} withdrawn successfully.")
        print("Update balance: Rs,",self.accounts[i].balance)

    def show_all_account(self):
        if self.total_accounts ==0:
            print("No accounts found.")
            return

        print("\n===== All Bank Accounts =====")
        for i in range(self.total_accounts):
            account = self.accounts[i]
            print(f"\nAccount {i + 1}")
            print("Name           :", account.name)
            print("Account Number :", account.account_number)
            print("Balance        : Rs.", account.balance)
random.seed(time.time())
bank = BankSystem()

while True:
    print("\n********** Banking Management System **********")
    print("1. Open New Account")
    print("2. View Account Details")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.create_account()
    elif choice == 2:
        bank.view_account()
    elif choice == 3:
        bank.deposit()
    elif choice == 4:
        bank.withdraw()
    elif choice == 5:
        bank.show_all_account()
    elif choice == 6:

        print("Logged out successfully.")
        break

    else:

        print("Invalid choice.")




















