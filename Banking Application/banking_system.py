
#parent class

class User:
    #constructor function
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    #print user details
    def show_details(self):
        print("\n----User Details----\n")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print()
    
#child class

class Bank(User):
    
    #child constructor function

    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    
    def check_balance(self):
        print("Available Balance : ",self.balance)
    
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(self.amount,"has been successfully deposited")
        self.check_balance()
    
    def withraw(self,amount):
        self.amount=amount
        if(self.amount>self.balance):
            print("Insuffcient Balance!")
        else:
            self.balance-=self.amount
            print(self.amount, "has been successfully withdrawn")
            self.check_balance()


name=input("Name: ")
age=int(input("Age: "))
gender=input("Gender: ")

per=Bank(name,age,gender)
per.show_details()

while(1):
    print("-----Operations Performed-----")
    print("1.Deposit\n2.Withraw\n3.Check Balance\n4.Quit")
    choice=int(input("So, what do you wanna do: "))
    if(choice==1):
        amount=int(input("Deposit Amount: "))
        per.deposit(amount)
       
    
    elif(choice==2):
        amount=int(input("Withdrawn Amount: "))
        per.withraw(amount)
    
    elif(choice==3):
        per.check_balance()
    
    elif(choice==4):
        break

    else:
        print("Invalid choice")
    

    