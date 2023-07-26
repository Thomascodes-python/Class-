import maskpass
class Bankingsys:
    def __init__(self,name,othernames,age,password) -> None:
        self.name = name
        self.age = age
        self.password = password

class Create_acct(Bankingsys):
    def __init__(self,name,othernames,password,age):
        self.name = name
        self.othernames = othernames

        # self.password = password...
        
        self.age = age

        
        # for 
        # self.acctnumber = acct

class Deposit(Bankingsys):
    def __init__ (self,balance,amount):
        self.amount = amount
        self.balance = balance
        # available_balance = self.balance - self.amount
         
class Withdraw(Bankingsys):
    def __init__(self,amount,balance):
        self.amount = amount
        self.balance = balance

class CheckDetails(Bankingsys):
    def __init__(self,name,password,othernames,age,balance):
        # balance = 0
        self.name = name
        self.age = password
        self.password = age
        self.othernames = othernames
        self.balance = balance

# class Checkbalance(Bankingsys):
    # def __init__(self, name, othernames, age, password) -> None:
        # super().__init__(name, othernames, age, password)


if __name__=="__main__":
    print("1)Create Account \n2)Login")
    user_opt = int(input("Enter Option By Choosing Number:"))
    if user_opt == 1:
        customer_name = str(input("Enter name:"))
        customer_othernames = str(input("Enter Othernames:"))
        customer_password = maskpass.askpass(mask="*")
        # customer_password = input("Enter Password:")
        customer_age = int(input("Enter Age:"))
        comfirm_password = maskpass.advpass("Comfirm Password:",mask="*")
        if customer_password == comfirm_password:
            print("YOU HAVE SUCESSFULLY CREAYED ACCTOUNT")
            pass
        else:
            print("COMFIRM PASSWORD IS NOT SAME WITH PASSWORD")
            print("TRY AGAIN")
            exit()
        # if 
        # if cus
        customer = Create_acct(customer_name,customer_othernames,customer_password,customer_age)
        print(f"Welcome {customer_name} and your password is {customer_password}")
        print(customer.__dict__)

        "\n"
        
        "\n"
        
        while True:
            "\n"
            print("1)Deposit \n2)Withdrawl \n3)Check Account Details \n4)Logout")
            customer_balance = 0
            option = int(input("Enter Option By Choosing Number:"))
            if option == 1:
                amount = float(input("Enter Amount To Deposit: $"))
                initial_balance = Deposit(customer_balance, amount)
                balance = customer_balance + amount

                print(f"You Deposited {amount}")
                print(f"Your Available balance is {balance}")

            elif option == 2:
                amount = float(input("Enter Amount To Withdraw: $"))
                withdraw = Withdraw(balance , amount)
                available_balance = (balance - amount)
                print(f"You Withdraw {amount}")
                print(f"Your Available balance is {available_balance}")
                # if ava

            elif option == 3:
                customer = CheckDetails(customer_name,customer_othernames,customer_password,customer_age,balance)
                print(f"Name:{customer_name} \tOthernames:{customer_othernames} \tPassword:{customer_password} \tAge:{customer_age} \tAvailable Balance:{available_balance}")
            elif option == 4:
                print(f"Goodbye {customer_name}")
                exit()
