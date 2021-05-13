import datetime
import uuid

current_date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

class BankAccount():


    def __init__(self, name=str(input('Name your account: ')), balance=float(input('Enter your balance: '))):
        self.name = name
        self.uu_id = uuid.uuid4()
        self.balance = balance
        self.transaction = []


    def deposit(self):
        amount = float(input('A commission of 1% is charged for the funds transfer. Enter the amount to deposit: '))

        self.balance = self.balance + amount - (amount * 0.01)
        self.transaction.append('Deposit Transaction: ')
        self.transaction.append(self.balance)
        print(f'Deposit is completed. Your current balance: {self.balance}. Transfer date: {current_date}')


    def funds_withdrawal(self):
        amount = float(input('A commission of 1% is charged for the funds transfer. Enter the amount to withdrawal: '))

        if (self.balance >= amount):
            self.balance = self.balance - amount - (amount * 0.01)
            self.transaction.append('Withdrawal Transaction: ')
            self.transaction.append(self.balance)
            print(f'Withdrawal is completed. Your current balance: {self.balance}. Transfer date: {current_date}')
        else:
            print('Your account has insufficient funds')


    def get_balance(self):
        print(f'Your current balance: {self.balance}. Operation time: {current_date}')


    def display(self):
        print('Your account information: ')
        print(f'1. Account Name: {self.name}')
        print(f'2. UUID: {self.uu_id}')
        print(f'3. Balance: {self.balance}')


    def account_transactions(self):
        self.transaction.append('Current Date: ')
        self.transaction.append(current_date)
        print(f'Account transactions: {self.transaction}')



account = BankAccount()
account.deposit()
account.funds_withdrawal()
account.get_balance()
account.display()
account.account_transactions()
