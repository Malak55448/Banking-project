import unittest

import bank.account as file 

class MyAccountTests(unittest.TestCase):
    def setUp(self):
      self.testAccount = file.Account(
         account_id=100,
         balance_checking=10, 
         balance_savings=10)

    def test_depositCheck(self):
       self.testAccount.deposit("checking",90)
       self.assertEqual(self.testAccount.balance_checking, 100)


    def test_withdrawCheck(self):
        self.testAccount.withdraw("checking", 5)
        self.assertEqual(self.testAccount.balance_checking, 5)
    
    def test_depositSavings(self):
        self.testAccount.deposit("savings", 40)
        self.assertEqual(self.testAccount.balance_savings, 50)

    
    def test_withdrawSavings(self):
        self.testAccount.withdraw("savings", 5)
        self.assertEqual(self.testAccount.balance_savings, 5)

    def test_transferCheckToSavings(self):
        self.testAccount.transfer("checking", "savings", 5) #transfer form checking --> savings
        self.assertEqual(self.testAccount.balance_checking, 5)
        self.assertEqual(self.testAccount.balance_savings, 15)

    def test_transferSavingsToCheck(self):
        self.testAccount.transfer("savings", "checking", 5)#transfer form savings  --> checking
        self.assertEqual(self.testAccount.balance_savings, 5)
        self.assertEqual(self.testAccount.balance_checking, 15)

if __name__ == "__main__":
    unittest.main()