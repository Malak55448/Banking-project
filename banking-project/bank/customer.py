class Customer:
    def __init__(self, account_id, first_name, last_name, password, checking_balance=0.0, savings_balance=0.0):
        self.account_id = account_id
        self.first_name = first_name  
        self.last_name = last_name
        self.password = password 
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)
        self.overdraft_count = 0
        self.is_active = True


    def VerifyPassword(self, password):
        return self.password == password
    

    def get_fullName1(self):
        return f"{self.first_name} {self.last_name}"
    

     # I combined the idea into a single function.
     # Full update: all values change => like test_five_UpdateBalances. 
     # Partial update: only the balance => like test_six_UpdateBalances_Partial.

    def update_Malak_Balances(self, checking_balance, savings_balance, overdraft_count=None, is_active=None):
      self.checking_balance = checking_balance
      self.savings_balance = savings_balance
      self.overdraft_count = overdraft_count if overdraft_count is not None else self.overdraft_count
      self.is_active = is_active if is_active is not None else self.is_active



    def to_dict(self):
        """Convert to a dictionary for saving in CSV"""
        return {
            'account_id': self.account_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'balance_checking': self.checking_balance,
            'balance_savings': self.savings_balance,
            'overdraft_count': self.overdraft_count,
            'is_active': self.is_active
        }
    
    def __str__(self):
        return f"Customer: {self.get_fullName1()} (ID: {self.account_id})"