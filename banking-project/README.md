# banking-project
🏦  ACME Bank - Python Banking System
A comprehensive banking management system built with Python using Test-Driven Development (TDD) principles. This system provides complete banking functionality for customers and cashiers with robust overdraft protection and data persistence.


🚀 Features
💳 Core Banking Operations

Account Management: Create checking and savings accounts with customizable initial balances
Secure Authentication: Password-protected account access with session management
Money Operations: Full deposit and withdrawal functionality with validation
Balance Inquiry: Real-time account balance checking with detailed information
Money Transfers: Between own accounts and to other customers

🛡️ Advanced Overdraft Protection

Smart Limits: Prevent excessive negative balances (minimum -$100)
Automatic Fees: $35 overdraft fee when limits are exceeded
Withdrawal Restrictions: Maximum $100 withdrawal when account is negative
Account Safety: Automatic deactivation after 2 overdrafts
Recovery System: Account reactivation when balance returns positive

💾 Data Management

CSV Persistence: All customer data stored and retrieved from CSV files
Data Integrity: Automatic synchronization between Account and Customer objects
Error Handling: Comprehensive exception handling for all operations

📁 Project Structure
banking_project/
├── bank/
│   ├── __init__.py
│   ├── account.py          # Account class with overdraft protection
│   ├── customer.py         # Customer information management
│   └── bank_system.py      # Main banking system controller
├── test/
│   ├── __init__.py
│   ├── test_account.py     # Account class unit tests
│   ├── test_customer.py    # Customer class unit tests  
│   └── test_bank_system.py # Integration tests
├── data/
│   └── bank.csv           # Customer data storage
├── main.py                # Terminal user interface
├── README.md              # Project documentation


🛠️ Installation & Usage
Prerequisites

Python 3.7+ installed on your system
Basic terminal/command line knowledge

💳 Default Test Accounts

Account IDNamePasswordCheckingSavings10001Suresh Sigerajuagw362$1,000$10,00010002James Tayloridh36%@#FGd$10,000$10,00010003Melvin GordonuYWE732g4ga1$2,000$20,00010004Stacey AbramsDEU8_qw3y72$$2,000$20,00010005Jake Pauld^dg23g)@$100,000$100,000



🧪 Testing Approach
This project was developed using Test-Driven Development (TDD):
TDD Process Followed:

✅ Red: Write failing tests first
✅ Green: Write minimum code to pass tests
✅ Refactor: Improve code while keeping tests passing
✅ Repeat: Continue for each new feature


Test Coverage:

Unit Tests: Individual class functionality testing
Integration Tests: Full system workflow testing
Edge Cases: Error conditions and boundary value testing
User Story Validation: Each requirement tested thoroughly

🔧 Technical Implementation
Architecture

Object-Oriented Design: Clean separation of concerns with dedicated classes
Data Persistence: CSV-based storage with automatic backup
Error Handling: Comprehensive exception management
Input Validation: All user inputs validated and sanitized

Key Classes

Account: Manages individual account operations with overdraft protection
Customer: Handles customer information and authentication
BankingSystem: Coordinates all operations and manages data persistence

Design Patterns Used

MVC Pattern: Separation of data (models), logic (controllers), and interface (views)
Repository Pattern: Data access abstraction through CSV handling
Strategy Pattern: Different account types with consistent interfaces

📋 Functional Requirements Met
✅ Customer Management

 Add new customers with checking accounts
 Add new customers with savings accounts
 Add new customers with both account types
 Automatic or manual account ID generation

✅ Banking Operations (Login Required)

 Withdraw from checking accounts
 Withdraw from savings accounts
 Deposit into checking accounts
 Deposit into savings accounts

✅ Money Transfers (Login Required)

 Transfer from savings to checking
 Transfer from checking to savings
 Transfer to another customer's account

✅ Overdraft Protection System

 $35 overdraft fee when account goes negative
 Prevent withdrawals > $100 when account is negative
 Prevent balances below -$100
 Deactivate accounts after 2 overdrafts
 Reactivate accounts when brought current

⚠️ Overdraft Protection Rules

Minimum Balance: Accounts cannot go below -$100
Overdraft Fee: $35 automatically charged for negative balances
Withdrawal Limits: Maximum $100 withdrawal when account is negative
Account Deactivation: Automatic after 2 overdrafts
Reactivation: Available when account balance becomes positive

🚦 System Behavior
Normal Operations

All deposits and withdrawals validated before processing
Real-time balance updates with automatic data persistence
Secure login sessions with proper logout functionality

Error Handling

Invalid login attempts blocked with clear error messages
Insufficient funds prevented with helpful guidance
Overdraft limits enforced with fee notifications
Account deactivation alerts with reactivation instructions

🔮 Future Enhancements

Transaction History: Detailed logging of all operations
Interest Calculation: Automatic interest on savings accounts
Mobile Interface: REST API for mobile applications
Advanced Reporting: Analytics and business intelligence
Multi-Currency: Support for different currencies
Automated Testing: CI/CD pipeline with automated test execution

👨‍💻 Development Information
Technologies Used:

Python 3.7+
CSV for data persistence
Object-oriented programming principles
Test-driven development methodology

Development Timeline:

Planning & Design: September 21, 2025
Core Development: September 22-25, 2025
Testing & Refinement: September 26-27, 2025
Final Integration: September 28, 2025


⚠️ Overdraft Protection Rules

Minimum Balance: Accounts cannot go below -$100
Overdraft Fee: $35 automatically charged for negative balances
Withdrawal Limits: Maximum $100 withdrawal when account is negative
Account Deactivation: Automatic after 2 overdrafts
Reactivation: Available when account balance becomes positive

🚦 System Behavior
Normal Operations

All deposits and withdrawals validated before processing
Real-time balance updates with automatic data persistence
Secure login sessions with proper logout functionality

Error Handling

Invalid login attempts blocked with clear error messages
Insufficient funds prevented with helpful guidance
Overdraft limits enforced with fee notifications
Account deactivation alerts with reactivation instructions

🔮 Future Enhancements

Transaction History: Detailed logging of all operations
Interest Calculation: Automatic interest on savings accounts
Mobile Interface: REST API for mobile applications
Advanced Reporting: Analytics and business intelligence
Multi-Currency: Support for different currencies
Automated Testing: CI/CD pipeline with automated test execution

👨‍💻 Development Information
Technologies Used:

Python 3.7+
CSV for data persistence
Object-oriented programming principles
Test-driven development methodology

Development Timeline:

Planning & Design: September 21, 2025
Core Development: September 22-25, 2025
Testing & Refinement: September 26-27, 2025
Final Integration: September 28, 2025