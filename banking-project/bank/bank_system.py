import csv
import os
import random
try:
    from bank.customer import Customer
    from bank.account import Account
except ImportError:
    from customer import Customer
    from account import Account

class BankingSystem:
    def __init__(self, csv_file_path="data/bank.csv"):
        self.csv_file_path = csv_file_path
        self.customers = {}
        self.accounts = {}
        self.current_user = None
        
        self._ensure_csv_exists()
        self._load_customers()
    
    def _ensure_csv_exists(self):
        os.makedirs(os.path.dirname(self.csv_file_path), exist_ok=True)
        
        if not os.path.exists(self.csv_file_path):
            self._create_initial_csv()
    
    def _create_initial_csv(self):
        with open(self.csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(['account_id', 'first_name', 'last_name', 'password', 
                           'balance_checking', 'balance_savings', 'overdraft_count', 'is_active'])
            
            sample_data = [
                ['10001', 'suresh', 'sigera', 'juagw362', '1000', '10000', '0', 'True'],
                ['10002', 'james', 'taylor', 'idh36%@#FGd', '10000', '10000', '0', 'True'],
                ['10003', 'melvin', 'gordon', 'uYWE732g4ga1', '2000', '20000', '0', 'True'],
                ['10004', 'stacey', 'abrams', 'DEU8_qw3y72$', '2000', '20000', '0', 'True'],
                ['10005', 'jake', 'paul', 'd^dg23g)@', '100000', '100000', '0', 'True']
            ]
            writer.writerows(sample_data)
    
    def _load_customers(self):
        try:
            with open(self.csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    account_id = row['account_id']
                    
                    customer = Customer(
                        account_id=account_id,
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        password=row['password'],
                        checking_balance=float(row['balance_checking']),
                        savings_balance=float(row['balance_savings'])
                    )
                    
                    if 'overdraft_count' in row and row['overdraft_count']:
                        customer.overdraft_count = int(row['overdraft_count'])
                    
                    if 'is_active' in row and row['is_active']:
                        customer.is_active = row['is_active'].lower() == 'true'
                    
                    self.customers[account_id] = customer
                    
                    account = Account(
                        account_id=account_id,
                        checking_balance=customer.checking_balance,
                        savings_balance=customer.savings_balance
                    )
                    account.overdraft_count = customer.overdraft_count
                    account.is_active = customer.is_active
                    
                    self.accounts[account_id] = account
                    
        except FileNotFoundError:
            print(f"CSV file not found: {self.csv_file_path}")
    
    def _save_customers(self):
        with open(self.csv_file_path, 'w', newline='') as file:
            fieldnames = ['account_id', 'first_name', 'last_name', 'password', 
                        'balance_checking', 'balance_savings', 'overdraft_count', 'is_active']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for customer in self.customers.values():
                writer.writerow(customer.to_dict())
    
    def _sync_customer_with_account(self, account_id):
        account = self.accounts[account_id]
        customer = self.customers[account_id]
        
        customer.update_Malak_Balances(
            account.checking_balance, 
            account.savings_balance,
            account.overdraft_count, 
            account.is_active
        )
    
    def generate_account_id(self):
        while True:
            account_id = str(random.randint(10000, 99999))
            if account_id not in self.customers:
                return account_id
    
    def add_customer(self, first_name, last_name, password, account_id=None, 
                    checking_balance=0.0, savings_balance=0.0):
        if not account_id:
            account_id = self.generate_account_id()
        
        if account_id in self.customers:
            raise Exception(f"Account ID {account_id} already exists")
        
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        
        if checking_balance < 0 or savings_balance < 0:
            raise ValueError("Initial balances cannot be negative")
        
        customer = Customer(
            account_id=account_id,
            first_name=first_name,
            last_name=last_name,
            password=password,
            checking_balance=checking_balance,
            savings_balance=savings_balance
        )
        
        account = Account(
            account_id=account_id,
            checking_balance=checking_balance,
            savings_balance=savings_balance
        )
        
        self.customers[account_id] = customer
        self.accounts[account_id] = account
        self._save_customers()
        
        return account_id
    
    def login(self, account_id, password):
        if account_id not in self.customers:
            raise Exception("Invalid account ID")
        
        customer = self.customers[account_id]
        if not customer.VerifyPassword(password): 
            raise Exception("Invalid password")
        
        self.current_user = account_id
        return True
    
    def logout(self):
        self.current_user = None
    
    def _require_login(self):
        if not self.current_user:
            raise Exception("Please login first")
    
    def deposit(self, account_type, amount):
        self._require_login()
        
        account = self.accounts[self.current_user]
        
        if account_type.lower() == 'checking':
            new_balance = account.deposit_checking(amount)
        elif account_type.lower() == 'savings':
            new_balance = account.deposit_savings(amount)
        else:
            raise ValueError("Account type must be 'checking' or 'savings'")
        
        self._sync_customer_with_account(self.current_user)
        self._save_customers()
        
        return new_balance
    
    def withdraw(self, account_type, amount):
        """سحب مبلغ"""
        self._require_login()
        
        account = self.accounts[self.current_user]
        
        if account_type.lower() == 'checking':
            new_balance = account.withdraw_checking(amount)
        elif account_type.lower() == 'savings':
            new_balance = account.withdraw_savings(amount)
        else:
            raise ValueError("Account type must be 'checking' or 'savings'")
        
        self._sync_customer_with_account(self.current_user)
        self._save_customers()
        
        return new_balance
    
    def transfer_between_own_accounts(self, from_account, to_account, amount):
        self._require_login()
        
        account = self.accounts[self.current_user]
        
        if from_account.lower() == 'checking' and to_account.lower() == 'savings':
            account.transfer_checkingTOsavings(amount)  
        elif from_account.lower() == 'savings' and to_account.lower() == 'checking':
            account.transfer_savingsTOchecking(amount) 
        else:
            raise ValueError("Invalid account types for transfer")
        
        self._sync_customer_with_account(self.current_user)
        self._save_customers()
        
        return True
    
    def transfer_to_another_customer(self, from_account_type, to_account_id, amount):
        self._require_login()
        
        if to_account_id not in self.customers:
            raise Exception("Recipient account not found")
        
        if to_account_id == self.current_user:
            raise Exception("Cannot transfer to your own account")
        
        sender_account = self.accounts[self.current_user]
        recipient_account = self.accounts[to_account_id]
        
        if from_account_type.lower() == 'checking':
            sender_account.withdraw_checking(amount)
        elif from_account_type.lower() == 'savings':
            sender_account.withdraw_savings(amount)
        else:
            raise ValueError("From account type must be 'checking' or 'savings'")
        
        recipient_account.deposit_checking(amount)
        
        self._sync_customer_with_account(self.current_user)
        self._sync_customer_with_account(to_account_id)
        self._save_customers()
        
        return True
    
    def get_balance(self):
        self._require_login()
        
        account = self.accounts[self.current_user]
        return {
            'checking': account.checking_balance,
            'savings': account.savings_balance,
            'total': account.get_total_balance(),
            'overdraft_count': account.overdraft_count,
            'is_active': account.is_active
        }
    
    def get_customer_info(self):
        self._require_login()
        
        customer = self.customers[self.current_user]
        return {
            'account_id': customer.account_id,
            'name': customer.get_fullName1(),  
            'first_name': customer.first_name,
            'last_name': customer.last_name
        }