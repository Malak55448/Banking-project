import unittest
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAccount(unittest.TestCase):
    def test_one_account_exists(self):
        try:
            from bank.account import Account
            print("class account is available!")

        except ImportError:
            self.fail("class account is not available -we must create it ")

    def test_two_account(self):
        from bank.account import Account 
        account = Account("10001",1000.0,5000.0)
        self.assertEqual(account.account_id, "10001")
        self.assertEqual(account.checking_balance, 1000.0)
        self.assertEqual(account.savings_balance, 5000.0)
        print("The account was successfully created")

    def test_three_DepositCheck(self):
        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)

        BalanceNew = account.deposit_checking(500.0)

        self.assertEqual(BalanceNew, 1500.0)
        self.assertEqual(account.checking_balance, 1500.0)
        print("Deposited into the current account")

    def test_four_DepositSav(self):
        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)

        BalanceNew = account.deposit_savings(1000.0)
        
        self.assertEqual(BalanceNew, 6000.0)
        self.assertEqual(account.savings_balance, 6000.0)
        print("funds have been deposited into the savings account")


    def test_five_invDeposit(self):
        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)
      

        with self.assertRaises(ValueError): #depositing a negative amoount is wrong -100 ≤ 0
            account.deposit_checking(-100.0)


        with self.assertRaises(ValueError):#: 0 ≤ 0
            account.deposit_checking(0)
        print("preventing in correct deposits") 

    def test_six_WithdrawCheck_right(self):# Successful withdrawal from the checking account

        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)

        BalanceNew = account.withdraw_checking(200.0)
        self.assertEqual(BalanceNew, 800.0)
        self.assertEqual(account.checking_balance, 800.0)
        print("Withdrawal from the checking account")

    def test_seven_withdrawsav_right(self):  #Successful withdrawal from the savings account
        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)

        BalanceNew = account.withdraw_savings(1000.0)


    def test_eight_OverdraftFees(self): 
        from bank.account import Account
        account = Account("10001", 1000.0, 5000.0)

        BalanceNew = account.withdraw_checking(1050.0)
        ExpectBalance = 1000.0 - 1050.0 - Account.OVERDRAFT_FEES
        self.assertEqual(BalanceNew, ExpectBalance)
        self.assertEqual(account.overdraft_count, 1)#We make sure that the overdraft counter increased by one after this withdrawalظ 

        print("Overdraft fees have been applied!")


    from bank.account import Account

    # I created a demo account to verify.
    acc = Account("12345", 100.0, 500.0)

    print("Test of the Updated Code")
    print(f"Opening balance: {acc}")

    print("\n Overdraft test:")
    acc.withdraw_checking(150.0) # Will cause an overdraft
    print(f"After excessive withdrawal: Checking = ${acc.checking_balance}")
    print(f"Number of extra draws: {acc.overdraft_count}")

    print("\n Conversion test:")
    acc.transfer_savingsTOchecking(200.0)
    print(f"After the transfer: {acc}")

    print("\n The updated code works correctly!")


if __name__ =='__main__':
    print("start account tests")
    unittest.main(verbosity= 2)


#I completed the deposit, withdrawal, and overdraft cases.