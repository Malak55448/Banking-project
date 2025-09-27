class Account:
    OVERDRAFT_FEES = 35.0
    MIN_ALLOWED_BALANCE = -100.0  # the minimum balance allowed 
    OVERDRAFT_WITHDRAWAL_LIMIT =100.0
    MAX_OVERDRAFT =2 # Maximum withdrawal at negative balance 
   
    #The new account is equipped with the basic features
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


      # Reactivating the account if the balance becomes positive
      if self.checking_balance >= 0 and not self.is_active:
            self.is_active = True

      return self.checking_balance
    
    def deposit_savings(self, amount):
      if amount <= 0:
        raise ValueError("the deposit amount must be greater then Zero")
      if not self.is_active:
        raise Exception("Account disabled-The operation cannot be completed.")
    
      self.savings_balance += amount
      return self.savings_balance
    
    def withdraw_checking(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if not self.is_active:
            raise Exception("Account disabled - cannot withdraw.")
        
        # Checking the withdrawal limit for overdrawn accounts
        if self.checking_balance < 0 and amount > self.OVERDRAFT_WITHDRAWAL_LIMIT:
            raise Exception(f"Cannot withdraw more than ${self.OVERDRAFT_WITHDRAWAL_LIMIT} when account is negative")
        
        # New Account Balance 
        new_balanceCH = self.checking_balance - amount

        if new_balanceCH < self.MIN_ALLOWED_BALANCE:
            raise Exception(f"Cannot withdraw - would exceed minimum balance of ${self.MIN_ALLOWED_BALANCE}")
        
        self.checking_balance = new_balanceCH


        if self.checking_balance < 0 and (self.checking_balance + amount) >= 0:
           self._handlingOverdraft()
        
        return self.checking_balance
    
                #if new_balanceCH < 0:
                #self.overdraft_count += 1   # Increase the overdraft counter
                #new_balanceCH -= Account.OVERDRAFT_FEES  # Overdraft fee application ,I finally understood it. '''
                    

    # Function to withdraw money from savings account 
    def withdraw_savings(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if not self.is_active:
            raise Exception("Account disabled - cannot withdraw.")

        if amount > self.savings_balance:
            raise Exception("Insufficient funds in savings account!") 
         
        self.savings_balance -= amount
        return self.savings_balance
    

    def transfer_checkingTOsavings(self, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")    
        if not self.is_active:
            raise Exception("Account disabled - cannot transfer")

        #Purpose: Transfer balance between checking and savings accounts.
        #Features: Uses the withdrawal function to check balance and activity.
        self.withdraw_checking(amount)
        self.savings_balance += amount
        
        return True

    def transfer_savingsTOchecking(self, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")
            
        if not self.is_active:
            raise Exception("Account disabled - cannot transfer")
        
        if amount > self.savings_balance:
            raise Exception("Insufficient funds in savings account")
        
        #Purpose: Convert the savings account to a current account and reactivate the account if it becomes positive.
        self.savings_balance -= amount
        self.checking_balance += amount

        if self.checking_balance >= 0 and not self.is_active:
            self.is_active = True
        
        return True



    # Applying fees and disabling the account after two withdrawals
    def _handlingOverdraft(self):
        self.overdraft_count += 1
        self.checking_balance -= self.OVERDRAFT_FEES
        
        print(f"Overdraft fee of ${self.OVERDRAFT_FEES} applied")
        
        if self.overdraft_count >= self.MAX_OVERDRAFT:
            self.is_active = False
            print(f"Account deactivated after {self.MAX_OVERDRAFT} overdrafts")


    # To reactivate the account upon payment of fees
    def pay_overdraft_fees(self):
        if self.checking_balance >= 0:
            self.overdraft_count = 0
            self.is_active = True
            print("Overdraft fees cleared, account reactivated")

            return True
        return False
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'balance_checking': self.checking_balance,
            'balance_savings': self.savings_balance,
            'overdraft_count': self.overdraft_count,
            'is_active': self.is_active
        }








    def get_total_balance(self):
      return self.checking_balance + self.savings_balance
    
    def __str__(self):
      return f"Account {self.account_id}: Checking=${self.checking_balance}, Savings=${self.savings_balance}"
    
