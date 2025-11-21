class BankAccount:
    def __init__(self,name,acc_number,balance,pin):
        self.name=name
        self.acc_number=acc_number
        self.balance=balance
        self.pin=pin

    def check_pin(self):
        enter_pin = int(input("ENTER PIN: "))
        if enter_pin == self.pin:
            return True
        else:
            print("you enter invalid pin please, return valid pin ")
            return False
        
    def deposit(self,ammount):
        enter_pin = int(input("ENTER PIN: "))
        if enter_pin == self.pin:
            self.balance += ammount
            print(f"{ammount} deposited successfully")
            print(f"your new balance after deposit is : {self.balance}")
        else:
            print("you enter invalid pin please, return valid pin ")
           
    def withdraw(self,ammount):
        enter_pin = int(input("ENTER PIN: "))
        if enter_pin != self.pin:
            print("you enter invalid pin please, enter valid pin ")
        elif ammount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= ammount
            print(f"{ammount} withdraw successfully")
            print(f"your new balance after withdraw is : {self.balance}")


    def __str__(self):
        return  (f"Account Holder name: {self.name}\n"f"Account Number: {self.acc_number}\n"f"Balance: {self.balance}")
        

account1 = BankAccount("ritu dhanani", "123456789", 1000, 1234)  
print(account1)
account1.deposit(500)
account1.withdraw(200)
print("final dteails of account after transactions: ")
print(account1)




