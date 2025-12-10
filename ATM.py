import sqlite3
import time as t

# ============ DATABASE SETUP =================
def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            pin INTEGER NOT NULL,
            balance INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

# Create a new account
def create_account():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    print("\n------ CREATE NEW ACCOUNT ------")
    name = input("Enter Account Holder Name: ")
    pin = int(input("Set 4-digit PIN: "))
    balance = int(input("Initial Deposit Amount: "))

    cursor.execute("INSERT INTO accounts (name, pin, balance) VALUES (?, ?, ?)",
                   (name, pin, balance))
    conn.commit()

    acc_no = cursor.lastrowid

    print(f"\nAccount Created Successfully! Your Account Number: {acc_no}")
    conn.close()

# Validate account using PIN
def verify_account():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    print("\n----------- LOGIN -----------")
    acc_no = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc_no, pin))
    result = cursor.fetchone()

    conn.close()
    return result  # Returns tuple (acc_no, name, pin, balance)

# Update balance or PIN in DB
def update_account(acc_no, field, value):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(f"UPDATE accounts SET {field}=? WHERE acc_no=?", (value, acc_no))
    conn.commit()
    conn.close()

# =========== ATM OPERATIONS =================
def atm_menu(account):
    acc_no, name, pin, balance = account

    print("\nWelcome", name)
    print("Please Insert your ATM Card...")
    t.sleep(2)

    print("""
    ------------ ATM MENU ------------
      1. Balance Inquiry
      2. Withdraw Amount
      3. Deposit Amount
      4. Change PIN
    """)

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Try again.")
        return

    # CASE 1: BALANCE INQUIRY
    if choice == 1:
        print(f"\nYour Current Balance: ₹{balance}")

    # CASE 2: WITHDRAW MONEY
    elif choice == 2:
        amt = int(input("Enter amount to withdraw: "))
        if amt > balance:
            print("Insufficient Balance!")
        else:
            balance -= amt
            update_account(acc_no, "balance", balance)
            print(f"\n₹{amt} Withdrawn Successfully!")
            print(f"Available Balance: ₹{balance}")

    # CASE 3: DEPOSIT MONEY
    elif choice == 3:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        update_account(acc_no, "balance", balance)
        print(f"\n₹{amt} Deposited Successfully!")
        print(f"Updated Balance: ₹{balance}")

    # CASE 4: CHANGE PIN
    elif choice == 4:
        new_pin = int(input("Enter New PIN: "))
        update_account(acc_no, "pin", new_pin)
        print("\nPIN Updated Successfully!")

    else:
        print("Invalid Option. Try Again.")

# ============== MAIN PROGRAM ===============
def main():
    init_db()

    while True:
        print("""
        =========================
             WELCOME TO ATM
        =========================
        1. Create New Account
        2. Use ATM (Login)
        3. Exit
        """)

        option = input("Enter your choice: ")

        if option == "1":
            create_account()

        elif option == "2":
            account = verify_account()
            if account:
                atm_menu(account)
            else:
                print("❌ Invalid Account Number or PIN. Try again.")

        elif option == "3":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid Option! Try Again.")

# Run program
main()
