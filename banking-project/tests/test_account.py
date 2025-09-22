import unittest

import bank.account as file 

class MyAccountTests(unittest.TestCase):
    def setUp(self):
      self.testAccount = file.Account(account_id=100, balance_checking=10, balance_savings=0)



