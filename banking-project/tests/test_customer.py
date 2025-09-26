
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMyCustomer(unittest.TestCase):

    def test_one_CustomerCreat(self):
        from bank.customer import Customer
        customer = Customer("10001", "Malak", "Ali", "malak123", 1000.0, 5000.0)

        self.assertEqual(customer.account_id, "10001")
        self.assertEqual(customer.first_name, "Malak")
        self.assertEqual(customer.last_name, "Ali") 
        self.assertEqual(customer.password, "malak123")
        self.assertEqual(customer.checking_balance, 1000.0)
        self.assertEqual(customer.savings_balance, 5000.0)
        self.assertEqual(customer.overdraft_count, 0)
        self.assertTrue(customer.is_active)
        print(" Customer created successfully!")


      #right password
    def test_two_VerifyPassword_right(self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Malak", "Ali", "malak123")
        self.assertTrue(customer.VerifyPassword("malak123"))
        print(" Password works!")

      #wrong password
    def test_three_VerifyPassword_wrong (self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Malak", "Ali", "malak123")
        
        self.assertFalse(customer.VerifyPassword("124mm"))
        self.assertFalse(customer.VerifyPassword(""))
        self.assertFalse(customer.VerifyPassword("123"))
        print(" Wrong password rejected!")

   #  get full name
    def test_four_getFullName(self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Malak", "Ali", "malak123")
        
        self.assertEqual(customer.get_fullName1(), "Malak Ali")
        print(" Full name works! got it!!!")


    def test_five_UpdateBalances(self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Malak", "Ali", "malak123", 1000.0, 5000.0)
        
        customer.update_Malak_Balances(1500.0, 4500.0, overdraft_count=1, is_active=False)
        
        self.assertEqual(customer.checking_balance, 1500.0)
        self.assertEqual(customer.savings_balance, 4500.0)
        self.assertEqual(customer.overdraft_count, 1)
        self.assertFalse(customer.is_active)
        print("Balance update works! goood :)")
    

    def test_six_UpdateBalances_Partial(self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Malak", "Ali", "malak123", 1000.0, 5000.0)
        
        customer.update_Malak_Balances(2000.0, 3000.0)
        
        self.assertEqual(customer.checking_balance, 2000.0)
        self.assertEqual(customer.savings_balance, 3000.0)
        self.assertEqual(customer.overdraft_count, 0)   
        self.assertTrue(customer.is_active)  
        print("  UpdateBalances_Partial works!")






        
if __name__ == '__main__':
    print("customer tests")
    unittest.main(verbosity=2) # verbosity=2 : prints the names of the tests one by one and shows whether each test passed (PASS) or failed (FAIL)
