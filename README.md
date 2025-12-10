**ATM Simulation Using Python**

  In today's digital world, ATM cards, debit cards, and POS machines are used everywhere—from shopping malls and petrol bunks to restaurants and retail stores. Earlier, people had to physically visit an ATM, stand in a queue, insert their card, and perform transactions manually.

  This project simulates the functioning of a real ATM using Python and SQLite database. It demonstrates how an ATM system handles account creation, authentication, balance management, withdrawals, deposits, and PIN updates. The system provides a realistic and secure ATM-like experience.

**How it works:**
**1. Account Creation**
Users can create a new bank account by entering:
1. Account Holder Name
2. 4-digit PIN
3. Initial Deposit Amount
Once created, the account is stored securely in the database with:

Auto-generated Account Number will appear

**2. Login & PIN Verification**
To access ATM features, user must:
1. Enter Account Number
2. Enter PIN
3. If the PIN matches the database record:
  Access is granted
Otherwise:
  The system displays “Invalid PIN” and denies access

**ATM Operations**
    After successful login, users can perform the following operations:
**1. Balance Inquiry**
    Displays the user’s current account balance stored in the database.
    
**2. Cash Withdrawal**
Allows users to withdraw a specific amount.
  The system ensures:
    There is sufficient balance
    The balance is updated in the database after withdrawal
    
**3. Deposit Amount**
    Users can deposit money into their account.
  The deposited amount is added to the existing balance and stored in the database.

**4. PIN Change**
    Users can update or reset their ATM PIN.
    The new PIN is securely saved in the database.

**ATM Flow Summary**
Insert card (simulated) → Enter Account Number
Enter PIN
  If PIN is valid → Show ATM Menu
Choose an option:
  1. Balance Inquiry
  2. Withdraw Amount
  3. Deposit Amount
  4. Change PIN
System performs the selected operation and updates the database accordingly.

**Key Features**
1. Realistic ATM simulation using Python
2. Secure PIN-based authentication
3. SQLite database for account storage
4. Persistent balance and PIN management
5. Clean, modular, and user-friendly design
