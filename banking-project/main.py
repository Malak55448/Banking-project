import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from bank.bank_system import BankingSystem

def print_header():
    print("\n" + "="*60)
    print(" Welcome to ACME Bank Management System")
    print("="*60)

def main_menu():
    print("\n" + "-"*40)
    print(" Main Menu")
    print("-"*40)
    print("1.  Login to Your Account")
    print("2.  Create New Customer Account") 
    print("3.  Exit")
    print("-"*40)

def customer_menu():
    print("\n" + "-"*50)
    print(" Banking Operations Menu")
    print("-"*50)
    print("1.  Check Account Balance")
    print("2.  Deposit Money")
    print("3.  Withdraw Money")
    print("4.  Transfer Between My Accounts") 
    print("5.  Transfer to Another Customer")
    print("6.  Logout")
    print("-"*50)

def get_account_type():
    while True:
        print("\nAccount Types:")
        print("- checking (Checking Account)")
        print("- savings (Savings Account)")
        account_type = input("Enter account type: ").strip().lower()
        
        if account_type in ['checking', 'savings']:
            return account_type
        print(" Invalid account type. Please enter 'checking' or 'savings'")

def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print(" Amount must be greater than 0")
                continue
            return amount
        except ValueError:
            print(" Please enter a valid number")

def handle_login(bank):
    print("\n Account Login")
    print("-" * 20)
    
    account_id = input("Account ID: ").strip()
    password = input("Password: ").strip()
    
    try:
        bank.login(account_id, password)
        customer_info = bank.get_customer_info()
        print(f"\n Welcome back, {customer_info['name']}!")  # Uses get_fullName1()
        print(f"Account ID: {customer_info['account_id']}")
        return True
    except Exception as e:
        print(f"\n Login failed: {e}")
        return False

def handle_create_customer(bank):
    print("\n Create New Customer Account")
    print("-" * 35)
    
    try:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        
        if not first_name or not last_name:
            print(" First name and last name are required")
            return
        
        password = input("Password (minimum 6 characters): ").strip()
        
        print("\n Initial Balances (optional - press Enter for $0)")
        checking_input = input("Initial Checking Balance: $").strip()
        checking = float(checking_input) if checking_input else 0.0
        
        savings_input = input("Initial Savings Balance: $").strip()  
        savings = float(savings_input) if savings_input else 0.0
        
        account_id = bank.add_customer(
            first_name, last_name, password,
            checking_balance=checking,
            savings_balance=savings
        )
        
        print(f"\n Account created successfully!")
        print(f" Your Account ID: {account_id}")
        print(f" Customer Name: {first_name} {last_name}")
        print(f" Initial Checking: ${checking:.2f}")
        print(f" Initial Savings: ${savings:.2f}")
        print("\n Please remember your Account ID for future logins!")
        
    except ValueError as e:
        print(f"\n Invalid input: {e}")
    except Exception as e:
        print(f"\n Account creation failed: {e}")

def handle_check_balance(bank):
    try:
        balance_info = bank.get_balance()
        customer_info = bank.get_customer_info()
        
        print(f"\n Account Balance for {customer_info['name']}")
        print("=" * 50)
        print(f" Checking Account: ${balance_info['checking']:,.2f}")
        print(f" Savings Account:  ${balance_info['savings']:,.2f}")
        print(f" Total Balance:    ${balance_info['total']:,.2f}")
        
        if balance_info['overdraft_count'] > 0:
            print(f"\n  Overdraft Count: {balance_info['overdraft_count']}/2")
            print(" Pay overdraft fees to avoid account deactivation")
        
        if not balance_info['is_active']:
            print("\n ACCOUNT STATUS: DEACTIVATED")
            print(" Account deactivated due to excessive overdrafts")
            print(" Bring account to positive balance to reactivate")
            
    except Exception as e:
        print(f"\n Error retrieving balance: {e}")

def handle_deposit(bank):
    print("\n Deposit Money")
    print("-" * 20)
    
    try:
        account_type = get_account_type()
        amount = get_positive_amount(f"Amount to deposit in {account_type}: $")
        
        new_balance = bank.deposit(account_type, amount)
        print(f"\n Deposit successful!")
        print(f" New {account_type} balance: ${new_balance:,.2f}")
        
    except Exception as e:
        print(f"\n Deposit failed: {e}")

def handle_withdraw(bank):
    print("\n Withdraw Money")
    print("-" * 20)
    
    try:
        account_type = get_account_type()
        amount = get_positive_amount(f"Amount to withdraw from {account_type}: $")
        
        new_balance = bank.withdraw(account_type, amount)
        print(f"\n Withdrawal successful!")
        print(f" New {account_type} balance: ${new_balance:,.2f}")
        
        if new_balance < 0:
            print(f"\n  Your account balance is now negative")
            print(" Overdraft fees may apply")
        
    except Exception as e:
        print(f"\n Withdrawal failed: {e}")

def handle_transfer_own_accounts(bank):
    """Uses your transfer functions: transfer_checkingTOsavings & transfer_savingsTOchecking"""
    print("\n Transfer Between Your Accounts")
    print("-" * 40)
    
    try:
        print("From account:")
        from_account = get_account_type()
        
        print("\nTo account:")
        to_account = get_account_type()
        
        if from_account == to_account:
            print(" Cannot transfer to the same account type")
            return
        
        amount = get_positive_amount(f"Amount to transfer from {from_account} to {to_account}: $")
        
        
        bank.transfer_between_own_accounts(from_account, to_account, amount)
        print(f"\n Transfer successful!")
        print(f" Transferred ${amount:,.2f} from {from_account} to {to_account}")
        
    except Exception as e:
        print(f"\n Transfer failed: {e}")

def handle_transfer_to_customer(bank):
    print("\n Transfer to Another Customer")
    print("-" * 40)
    
    try:
        from_account = get_account_type()
        to_account_id = input("Recipient Account ID: ").strip()
        
        if not to_account_id:
            print(" Recipient Account ID is required")
            return
        
        amount = get_positive_amount(f"Amount to transfer from your {from_account}: $")
        
        print(f"\n Transfer Confirmation:")
        print(f"From: Your {from_account} account")
        print(f"To: Account ID {to_account_id}")
        print(f"Amount: ${amount:,.2f}")
        
        confirm = input("\nConfirm transfer? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print(" Transfer cancelled")
            return
        
        bank.transfer_to_another_customer(from_account, to_account_id, amount)
        print(f"\n Transfer successful!")
        print(f" Sent ${amount:,.2f} to Account ID {to_account_id}")
        
    except Exception as e:
        print(f"\n Transfer failed: {e}")

def main():
    print_header()
    print(" Starting ACME Bank System...")
    
    try:
        bank = BankingSystem()
        print(" Banking system initialized successfully")
    except Exception as e:
        print(f" Failed to initialize banking system: {e}")
        return
    
    while True:
        try:
            if not bank.current_user:
                main_menu()
                choice = input("Choose an option (1-3): ").strip()
                
                if choice == "1":
                    handle_login(bank)
                    
                elif choice == "2":
                    handle_create_customer(bank)
                    
                elif choice == "3":
                    print("\n Thank you for using ACME Bank!")
                    print(" Have a great day!")
                    break
                    
                else:
                    print(" Invalid choice. Please select 1-3.")
                    
            else:
                customer_menu()
                choice = input("Choose an option (1-6): ").strip()
                
                if choice == "1":
                    handle_check_balance(bank)
                    
                elif choice == "2":
                    handle_deposit(bank)
                    
                elif choice == "3":
                    handle_withdraw(bank)
                    
                elif choice == "4":
                    handle_transfer_own_accounts(bank) 
                    
                elif choice == "5":
                    handle_transfer_to_customer(bank)
                    
                elif choice == "6":
                    customer_info = bank.get_customer_info()
                    bank.logout()
                    print(f"\n Goodbye {customer_info['name']}!") 
                    print(" Thank you for banking with ACME!")
                    
                else:
                    print("Invalid choice. Please select 1-6.")
                    
        except KeyboardInterrupt:
            print("\n\n System shutdown requested.")
            print(" Thank you for using ACME Bank!")
            break
        except Exception as e:
            print(f"\n Unexpected error: {e}")
            print(" Please try again or contact support.")

if __name__ == "__main__":
    main()