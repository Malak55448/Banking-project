

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tempfile
import csv

from bank.bank_system import BankingSystem

class BankingSystem(unittest.TestCase):
    
    def setUp(self):
        """Setup temporary test environment"""
        # Create temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.temp_file.close()
        
        self.bank = BankingSystem(self.temp_file.name)
    
    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_01_system_creation(self):
        self.assertIsInstance(self.bank, BankingSystem)
        self.assertEqual(len(self.bank.customers), 5)  # default test customers
        self.assertEqual(len(self.bank.accounts), 5)
        self.assertIsNone(self.bank.current_user)
        print(" Banking system created successfully!")
    
    def test_02_csv_file_creation(self):
        self.assertTrue(os.path.exists(self.temp_file.name))
        
        # Read file and check content
        with open(self.temp_file.name, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
        self.assertEqual(len(rows), 5)  # 5 default customers
        self.assertIn('account_id', rows[0])
        self.assertIn('frst_name', rows[0])
        print(" CSV file created successfully!")
    
    def test_03_login_success(self):
        """Test 3: Successful login"""
        success = self.bank.login("10001", "juagw362")
        self.assertTrue(success)
        self.assertEqual(self.bank.current_user, "10001")
        print(" Login successful!")
    
    def test_04_login_invalid_id(self):
        """Test 4: Login with invalid account ID"""
        with self.assertRaises(Exception) as context:
            self.bank.login("99999", "anypassword")
        
        self.assertIn("Invalid account ID", str(context.exception))
        self.assertIsNone(self.bank.current_user)
        print(" Login blocked for invalid account ID!")
    
    def test_05_login_invalid_password(self):
        """Test 5: Login with invalid password"""
        with self.assertRaises(Exception) as context:
            self.bank.login("10001", "wrongpassword")
        
        self.assertIn("Invalid password", str(context.exception))
        self.assertIsNone(self.bank.current_user)
        print("✓ Login blocked for wrong password!")
    
    def test_06_logout(self):
        """Test 6: Logout"""
        self.bank.login("10001", "juagw362")
        self.assertEqual(self.bank.current_user, "10001")
        
        self.bank.logout()
        self.assertIsNone(self.bank.current_user)
        print("Logout successful!")
    
    def test_07_require_login_protection(self):
        """Test 7: Protect operations that require login"""
        with self.assertRaises(Exception) as context:
            self.bank.get_balance()
        self.assertIn("Please login first", str(context.exception))
        
        with self.assertRaises(Exception):
            self.bank.deposit("checking", 100.0)
            
        with self.assertRaises(Exception):
            self.bank.withdraw("savings", 50.0)
        
        print("Protected operations requiring login!")
    
    def test_08_get_balance(self):
        self.bank.login("10001", "juagw362")
        
        balance = self.bank.get_balance()
        
        self.assertIn('checking', balance)
        self.assertIn('savings', balance)
        self.assertIn('total', balance)
        self.assertIn('overdraft_count', balance)
        self.assertIn('is_active', balance)
        
        self.assertEqual(balance['checking'], 1000.0)
        self.assertEqual(balance['savings'], 10000.0)
        self.assertEqual(balance['total'], 11000.0)
        print(" Balance retrieved successfully!")
    
    def test_09_get_customer_info(self):
        self.bank.login("10001", "juagw362")
        
        info = self.bank.get_customer_info()
        
        self.assertEqual(info['account_id'], "10001")
        self.assertEqual(info['name'], "suresh sigera")
        self.assertEqual(info['first_name'], "suresh")
        self.assertEqual(info['last_name'], "sigera")
        print(" Customer information retrieved successfully!")
    
    def test_10_deposit_checking(self):
        self.bank.login("10001", "juagw362")
        
        new_balance = self.bank.deposit("checking", 500.0)
        self.assertEqual(new_balance, 1500.0)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['checking'], 1500.0)
        print(" Deposit into checking account successful!")
    
    def test_11_deposit_savings(self):
        self.bank.login("10001", "juagw362")
        
        new_balance = self.bank.deposit("savings", 1000.0)
        self.assertEqual(new_balance, 11000.0)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['savings'], 11000.0)
        print(" Deposit into savings account successful!")
    
    def test_12_deposit_invalid_account_type(self):
        self.bank.login("10001", "juagw362")
        
        with self.assertRaises(ValueError) as context:
            self.bank.deposit("invalid", 100.0)
        
        self.assertIn("Account type must be 'checking' or 'savings'", str(context.exception))
        print("Deposit blocked for invalid account type!")
    
    def test_13_withdraw_checking(self):
        self.bank.login("10001", "juagw362")
        
        new_balance = self.bank.withdraw("checking", 200.0)
        self.assertEqual(new_balance, 800.0)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['checking'], 800.0)
        print(" Withdraw from checking account successful!")
    
    def test_14_withdraw_savings(self):
        self.bank.login("10001", "juagw362")
        
        new_balance = self.bank.withdraw("savings", 1000.0)
        self.assertEqual(new_balance, 9000.0)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['savings'], 9000.0)
        print(" Withdraw from savings account successful!")
    
    def test_15_overdraft_scenario(self):
        self.bank.login("10001", "juagw362")
        
        new_balance = self.bank.withdraw("checking", 1050.0)
        expected_balance = 1000.0 - 1050.0 - 35.0
        self.assertEqual(new_balance, expected_balance)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['overdraft_count'], 1)
        self.assertTrue(balance_info['is_active'])
        print(" Overdraft scenario tested successfully!")
    
    def test_16_transfer_between_own_accounts_savings_to_checking(self):
        self.bank.login("10001", "juagw362")
        
        success = self.bank.transfer_between_own_accounts("savings", "checking", 500.0)
        self.assertTrue(success)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['savings'], 9500.0)
        self.assertEqual(balance_info['checking'], 1500.0)
        print("Transfer from savings to checking successful!")
    
    def test_17_transfer_between_own_accounts_checking_to_savings(self):
        self.bank.login("10001", "juagw362")
        
        success = self.bank.transfer_between_own_accounts("checking", "savings", 300.0)
        self.assertTrue(success)
        
        balance_info = self.bank.get_balance()
        self.assertEqual(balance_info['checking'], 700.0)
        self.assertEqual(balance_info['savings'], 10300.0)
        print("Transfer from checking to savings successful!")
    
    def test_18_transfer_invalid_account_types(self):
        self.bank.login("10001", "juagw362")
        
        with self.assertRaises(ValueError):
            self.bank.transfer_between_own_accounts("invalid", "checking", 100.0)
            
        with self.assertRaises(ValueError):
            self.bank.transfer_between_own_accounts("checking", "checking", 100.0)
        print("Transfers with invalid account types blocked!")
    
    def test_19_transfer_to_another_customer(self):
        self.bank.login("10001", "juagw362")
        
        success = self.bank.transfer_to_another_customer("checking", "10002", 200.0)
        self.assertTrue(success)
        
        sender_balance = self.bank.get_balance()
        self.assertEqual(sender_balance['checking'], 800.0)
        
        self.bank.logout()
        self.bank.login("10002", "idh36%@#FGd")
        recipient_balance = self.bank.get_balance()
        self.asserttEqual(recipient_balance['checking'], 10200.0)








if __name__ == '__main__':
    sys.argv = [sys.argv[0]]  # ignore any additional arguments
    unittest.main(verbosity=2)