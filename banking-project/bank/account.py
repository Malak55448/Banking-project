class Account:
    OVERDRAFT_FEES = 35.0
    MIN_ALLOWED_BALANCE = -100.0  # the minimum balance allowed 
    OVERDRAFT_WITHDRAWAL_LIMIT =100.0
    MAX_OVERDRAFT =2 # Maximum withdrawal at negative balance 
   
   
    def __init__(self,account_id ,checking_balance=0.0 ,savings_balance=0.0):

        self.account_id = account_id
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)
        self.overdraft_count = 0
        self.is_active = True  

    def deposit_checking(self, amount):
      if amount <= 0:
        raise ValueError("the deposit amount must be greater then Zero")
    
      if not self.is_active:
        raise Exception("Account disabled-The operation cannot be completed.")
    
      self.checking_balance += amount
      return self.checking_balance
    
    def deposit_savings(self, amount):
      if amount <= 0:
        raise ValueError("the deposit amount must be greater then Zero")
    
      if not self.is_active:
        raise Exception("Account disabled-The operation cannot be completed.")
    
      self.savings_balance += amount
      return self.savings_balance
    
    def get_total_balance(self):
     return self.checking_balance + self.savings_balance
    
    def __str__(self):
     return f"Account {self.account_id}: Checking=${self.checking_balance}, Savings=${self.savings_balance}"
