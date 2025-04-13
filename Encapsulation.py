Encapsulation:

#Banking Example:
    # Implement the BankAccount class appropriately

class BankAccount:
    def __init__(self, name, account_number, email, balance):
        self.name = name
        self.__account_number =account_number
        self.__email = email
        self.__balance = balance
        
    def set_account_number(self,get_account_number):
        self.__account_number = get_account_number
    
    def get_account_number(self):
        return (self.__account_number)
        
    def set_email(self,new_email):
        self.__email = new_email
        
    def get_email(self):
        return (self.__email)
        
    def set_balance(self,new_balance):
        if new_balance >=0:
            self.__balance  = new_balance
        else:
            return "The balance cannot be negative"
        
    def get_balance(self):
       return (self.__balance)
     
    def deposit_amount(self,amount,deposit_account_number):
        if(self.__account_number == deposit_account_number):
            if(amount >= 0):
                self.__balance += amount
            else:
                return "The deposit amount cannot be negative"
        else:
            return "Invalid account number"
    
    def withdraw_amount(self,amount,withdrawal_account_number):
        if(self.__account_number == withdrawal_account_number):
            if(amount >=0):
                if(self.__balance >= amount):
                    self.__balance -= amount
                else:
                    return "Insufficient funds for the transaction"
            else:
                return "The withdrawal amount cannot be negative"
        else:
            return "Invalid account number"
            
    
    
    

# Do not change any code below.
# Do not call this function anywhere.

def main():
    name = input()
    account_number = input()
    email = input()
    balance = int(input())
    new_account_number = input()
    new_email = input()
    new_balance = int(input())
    deposit_details = input()
    withdrawal_details = input()
    
    account = BankAccount(name, account_number, email, balance)
    
    account.set_email(new_email)
    print(account.get_email())
    
    account.set_account_number(new_account_number)
    print(account.get_account_number())
    
    error_message = account.set_balance(new_balance)
    if error_message:
        print(error_message)
    else:
        print(account.get_balance())

    
    amount, deposit_account_number = deposit_details.split() 
    error_message = account.deposit_amount(int(amount), deposit_account_number)
    if error_message:
        print(error_message)
    else:
        print(account.get_balance())

    amount, withdrawal_account_number = withdrawal_details.split()
    error_message = account.withdraw_amount(int(amount), withdrawal_account_number)
    if error_message:
        print(error_message)
    else:
        print(account.get_balance())

main()



# Vehilce :
    # Implement the Vehicle and Car classes appropriately
    
    class Vehicle:
        def __init__(self, manufacturer, model):
            self.manufacturer = manufacturer
            self.model = model
            
        def get_vehicle_info(self):
            return (f"Vehicle Manufacturer: {self.manufacturer}, Model: {self.model}")
            
    
    class Car(Vehicle):
        def __init__(self, manufacturer, model, manufacturing_year, engine):
            super().__init__(manufacturer, model)
            self.__manufacturing_year = manufacturing_year
            self.__engine = engine
        
        def set_manufacturing_year(self,new_manufacturing_year):
            self.__manufacturing_year = new_manufacturing_year
        
        def get_manufacturing_year(self):
            return (self.__manufacturing_year)
        
        def set_engine_type(self,new_engine):
            self.__engine = new_engine
        
        def get_engine_type(self):
            return (self.__engine)
            
        def get_car_info(self):
            return (f"{self.get_vehicle_info()}, Manufacturing Year: {self.__manufacturing_year}, Engine Type: {self.__engine}")
            
        
        
    
    # Do not change any code below.
    # Do not call this function anywhere.
    
    def main():
        manufacturer = input()
        model = input()
        manufacturing_year = int(input())
        engine = input()
        new_manufacturing_year = int(input())
        new_engine = input()
        
        car = Car(manufacturer, model, manufacturing_year, engine)
        car.set_manufacturing_year(new_manufacturing_year)
        car.set_engine_type(new_engine)
        print(car.get_car_info())
    
    main()
    
     
