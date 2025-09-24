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
if __name__ =='__main__':
    print("start account tests")
    unittest.main(verbosity= 2)
