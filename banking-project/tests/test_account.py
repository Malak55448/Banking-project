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


if __name__ =='__main__':
    print("start account tests")
    unittest.main(verbosity= 2)
