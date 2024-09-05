"""ATM Stimulation allows you to See your Account Balance, Withdraw amount, Deposit amount and Changing PIN
and it gives you Real time ATM Stimulation
Balance Inquiry: Users can check their current account balance.
Cash Withdrawal: Users can withdraw funds from their account by specifying an amount.
Deposit: Users can deposit funds into their account, either virtually or by simulating check or cash deposits.
PIN change: Users can Update their PIN if they Forgot.
"""

# importing libraries
import time as t
print('Please Insert your ATM Card')

# The ATM waits for 5 seconds for the user to insert their ATM card
t.sleep(5)

# Account Password
password = 7431
pin =  int(input('Please Enter your password: '))

# Account current balance
acc_balance = 5000

# If Acount PIN is true then It proceed the further process otherwise it deneid the access
if pin == password:

        #Using switch case to Process our requrements
        print("""
              1 Balance
              2 Withdraw amount
              3 Deposit amount
              4 PIN Change
              """)

        try: 
            value = int(input('Enter the choice: '))
        except:
            print('Invalid, Please enter a valid choice')

        # Enter the valid number to switch the respected choice of the user
        match value:
            case 1: 
                print(f"Your account balance is {acc_balance}")

            case 2: 
                  req_amount = int(input('Please enter amount in 500 and 100 only: '))
                  if req_amount > acc_balance: print('Insuficient amount')
                  else:
                        acc_balance = acc_balance - req_amount
                        print(f'Withdrawn amount {req_amount}')
                        print(f'Current Balance {acc_balance}')
                        print('Please collect Cash')

            case 3:
                  deposit_amt = int(input('Please enter amount '))
                  acc_balance+=deposit_amt
                  print(f'Deposit amount {deposit_amt}')
                  print(f'Current Balance {acc_balance}')

            case 4:
                    new_pin = int(input('Please enter your New PIN '))
                    pin = new_pin
                    print(f'Updated PIN {pin}')
                    print('PIN changed Successfully !!!')

            case _:
                    print('Invalid, Please enter valid option')

else:
    print('Invalid PIN, Try again')
