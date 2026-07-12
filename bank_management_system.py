# ==========================================
#        BANK MANAGEMENT SYSTEM
# ==========================================

accounts = []


# ------------------------------------------
# Create Account
# ------------------------------------------
def create_account():
    print("\n===== Create New Account =====")

    acc_no = input("Account Number: ")

    # Check duplicate account
    for account in accounts:
        if account["Account No"] == acc_no:
            print("❌ Account already exists.")
            return

    name = input("Account Holder Name: ")
    mobile = input("Mobile Number: ")
    balance = float(input("Opening Balance: ₹"))

    account = {
        "Account No": acc_no,
        "Name": name,
        "Mobile": mobile,
        "Balance": balance
    }

    accounts.append(account)

    print("\n✅ Account Created Successfully!")


# ------------------------------------------
# View All Accounts
# ------------------------------------------
def view_accounts():

    if len(accounts) == 0:
        print("\nNo Accounts Found.")
        return

    print("\n========== ACCOUNT LIST ==========")

    for account in accounts:

        print(f"""
Account No : {account['Account No']}
Name       : {account['Name']}
Mobile     : {account['Mobile']}
Balance    : ₹{account['Balance']:.2f}
-----------------------------------------
""")


# ------------------------------------------
# Search Account
# ------------------------------------------
def search_account():

    acc_no = input("\nEnter Account Number: ")

    for account in accounts:

        if account["Account No"] == acc_no:

            print("\nAccount Found")
            print("--------------------------")
            print("Account No :", account["Account No"])
            print("Name       :", account["Name"])
            print("Mobile     :", account["Mobile"])
            print("Balance    : ₹", account["Balance"])

            return

    print("❌ Account Not Found.")


# ------------------------------------------
# Deposit Money
# ------------------------------------------
def deposit():

    acc_no = input("\nEnter Account Number: ")

    for account in accounts:

        if account["Account No"] == acc_no:

            amount = float(input("Enter Deposit Amount: ₹"))

            account["Balance"] += amount

            print(f"\n✅ ₹{amount:.2f} Deposited Successfully.")
            print(f"Current Balance: ₹{account['Balance']:.2f}")

            return

    print("❌ Account Not Found.")


# ------------------------------------------
# Withdraw Money
# ------------------------------------------
def withdraw():

    acc_no = input("\nEnter Account Number: ")

    for account in accounts:

        if account["Account No"] == acc_no:

            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount > account["Balance"]:
                print("❌ Insufficient Balance.")
            else:
                account["Balance"] -= amount
                print(f"\n✅ ₹{amount:.2f} Withdrawn Successfully.")
                print(f"Remaining Balance: ₹{account['Balance']:.2f}")

            return

    print("❌ Account Not Found.")


# ------------------------------------------
# Transfer Money
# ------------------------------------------
def transfer_money():

    sender = input("\nSender Account Number: ")
    receiver = input("Receiver Account Number: ")

    sender_acc = None
    receiver_acc = None

    for account in accounts:

        if account["Account No"] == sender:
            sender_acc = account

        if account["Account No"] == receiver:
            receiver_acc = account

    if sender_acc is None or receiver_acc is None:
        print("❌ Invalid Account Number.")
        return

    amount = float(input("Enter Amount: ₹"))

    if amount > sender_acc["Balance"]:
        print("❌ Insufficient Balance.")
        return

    sender_acc["Balance"] -= amount
    receiver_acc["Balance"] += amount

    print("\n✅ Money Transferred Successfully.")


# ------------------------------------------
# Delete Account
# ------------------------------------------
def delete_account():

    acc_no = input("\nEnter Account Number: ")

    for account in accounts:

        if account["Account No"] == acc_no:
            accounts.remove(account)
            print("✅ Account Deleted Successfully.")
            return

    print("❌ Account Not Found.")


# ------------------------------------------
# Total Bank Balance
# ------------------------------------------
def total_balance():

    total = 0

    for account in accounts:
        total += account["Balance"]

    print(f"\nTotal Money in Bank: ₹{total:.2f}")


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("""
========================================
      BANK MANAGEMENT SYSTEM
========================================
1. Create Account
2. View All Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Transfer Money
7. Delete Account
8. Total Bank Balance
9. Exit
========================================
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        deposit()

    elif choice == "5":
        withdraw()

    elif choice == "6":
        transfer_money()

    elif choice == "7":
        delete_account()

    elif choice == "8":
        total_balance()

    elif choice == "9":
        print("\nThank You for Using Bank Management System!")
        break

    else:
        print("❌ Invalid Choice. Please Try Again.")