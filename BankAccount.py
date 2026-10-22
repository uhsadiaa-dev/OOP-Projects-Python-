#BankAccount 
class BankAccount:
     def __init__(self,name="",initialbalance=""):
        self.name = name
        self.initialbalance = initialbalance

     def __str__(self):
        return f"Account name:{self.name}\nBalance:{self.initialbalance}"


     def options(self):
               print("=========hello to happy bank=========")
               print("1.Create an account")
               print("2.Your current info")
               print("3.I want to deposit .")
               print("4.I want to withdraw ")
               print("5.I want to exit.")
     

     def create(self):#1
               self.name =input("Enter your name:")
               while True:
                    try:
                         self.initialbalance = float(input("Enter the ammount for ur account :"))   
                    except ValueError:
                         print("Please enter in numbers.")  
                         continue
                    break
               return  f"Account name:{self.name}\nBalance:{self.initialbalance}"

     def currentinfo(self):#2
              print(self)
     
     
     def deposit(self):#3
       
        if not self.name:
             print("you don't have a balance")
             return Account.create()
        else:
          print(self.initialbalance,"this is your current balance")
          depo = float(input("Enter the ammount you want to deposit:$"))
          self.initialbalance+=depo
          print("This is your ammount:$",self.initialbalance)
          
           
     def withdraw(self):#5
          print("Your current balance:$",self.initialbalance)
          remove = float(input("Enter The ammount:"))
          if remove > self.initialbalance:
              print( "Sorry! but your current ammount is short.")
          else:
               self.initialbalance -= remove 
               print("Your current balance :$",self.initialbalance)
               
#process
Account = BankAccount()
while True:
    Account.options()
    try:
       choice = int(input("choose :"))
    
       if choice == 1:
               Account.create()
       elif choice==2:
               Account.currentinfo()
       elif choice == 3:
               Account.deposit()
       elif choice ==4:
              Account.withdraw()
       elif choice ==5:
             print("Bye Bye")
             break
       else:
            print("invalid choice ")

    except ValueError:
           print("pls enter a whole number.")
 
       