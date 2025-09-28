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
