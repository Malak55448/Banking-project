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