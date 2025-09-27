
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
    

    def test_seven_Customer_object_ToDictionary(self):
        from bank.customer import Customer

        customer = Customer("10001", "Malak", "Ali", "malak123", 1000.0, 5000.0)
        customer.overdraft_count = 2
        customer.is_active = False
        
        expected_dict = {
        'account_id': "10001",
        'first_name': "Malak",
        'last_name': "Ali",
        'password': "malak123",
        'balance_checking': 1000.0,
        'balance_savings': 5000.0,
        'overdraft_count': 2,
        'is_active': False
        }

        self.assertDictEqual(customer.to_dict(), expected_dict)



    def test_eight_customer_Zero_balances(self):
        from bank.customer import Customer
        
        customer = Customer("10002", "Maha", "Naif", "123mm")
        
        self.assertEqual(customer.checking_balance, 0.0)
        self.assertEqual(customer.savings_balance, 0.0)
        self.assertTrue(customer.is_active)
        self.assertEqual(customer.overdraft_count, 0)
        print(" test_eight_customer_Zero_balances works!")
    
    def test_Nine_str_representation(self):
        from bank.customer import Customer
        
        customer = Customer("10001", "Amal", "Ali", "amal234")
        
        Information = "Customer: Amal Ali (ID: 10001)"
        self.assertEqual(str(customer), Information)
        print(" String representation works!")
    
    def test_Ten_cases(self):
        from bank.customer import Customer
        
                                 # Empty Names
        customer = Customer("10003", "", "", "pass123")
        self.assertEqual(customer.get_fullName1(), " ")
        
                      # Empty password
        customer2 = Customer("10004", "Test", "User", "")
        self.assertTrue(customer2.VerifyPassword(""))
        self.assertFalse(customer2.VerifyPassword("anything"))
        
        print(" Edge cases handled!")

        
if __name__ == '__main__':
    print("customer tests")
    unittest.main(verbosity=2) # verbosity=2 : prints the names of the tests one by one and shows whether each test passed (PASS) or failed (FAIL)
