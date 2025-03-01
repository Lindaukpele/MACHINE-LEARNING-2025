
import random

class BankAccount:
    def __init__(self, customer_id, account_number, customer_name, account_type, balance=0):
        self.customer_id = customer_id
        self.account_number = account_number
        self.customer_name = customer_name
        self.account_type = account_type
        self.balance = balance
        
    
    def generate_id(self):
        customer_id = random.randint(100, 9999)
        return self.customer_id
    
    def generate_account_number(self):
        account_number = random.randint(1234567, 999999)   #how do i increase the random digit by one or how do i make it orderly instead of random digit
        return self.account_number
    
    def acc_type(self, account_type):
        if account_type == 'Chequing':
            return 'Chequing'
        else:
            return 'Savings' 

    def deposit(self, cash_deposit):
        if cash_deposit > 0: 
            self.balance = self.balance + cash_deposit 
            print(f"Deposit successful. Your new balance is: {self.balance}")
        else:
            print("Invalid transaction")
    
    def withdrawal(self, balance):
        withdraw_amount = 0
        if withdraw_amount <= balance:
            print(f"Your available balance is: {balance}")
        else:
            print("Insufficient balance")
    
customer_1 = BankAccount('customer_id', 'account_number', 'Linda Ukpele', '1', 0)
customer_2 = BankAccount('customer_id', 'account_number', 'James Mora', '0', 0)

#customer_1.account_details()
customer_1.generate_id()
customer_1.generate_account_number()
customer_1.deposit(200)
customer_1.balance()
customer_1.withdraw(50)
customer_1.balance()

BankAccount()



        



