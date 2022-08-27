# Create 3 objects: bank, clock, objectives
# bank: Contains the current balance and a log of transactions. It also has a limit of 4 withdrawals per month. These is a $5 fee for each withdrawal.
# clock: keeps track of the day and decreases the balance by %0.005 every day. The clock handles the save file.
# objectives: contains the list of possible objectives. Some objectives are daily.

import datetime as dt
# save file
import pickle
import time as t



# Create bank object
class Bank:
    def __init__(self, balance = 0.0):
        self.balance = balance
        self.withdraw = []
        self.deposits = []
        self.withdraw_count = 0
        self.withdraw_limit = 4
        self.withdraw_fee = 5
        self.can_withdraw = False
        
    def withdrawel(self, amount):
        if self.withdraw_count < self.withdraw_limit and self.can_withdraw is True:
            self.balance -= amount
            self.withdraw_count += 1
            self.withdraw.append(amount)
        elif self.withdraw_count >= self.withdraw_limit:
            print("You have reached your withdraw limit.")
        elif self.can_withdraw == False:
            print("It costs $5 to withdraw. Would you like to pay $5 to withdraw?")
            answer = input("(y/n)")
            if answer == "y":
                self.balance -= self.withdraw_fee
                self.withdraw_count += 1
                self.withdraw.append(amount)
                self.can_withdraw = True
            

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append(amount)

    # given a date, reduce the balance by %0.005 every day until the current date is reached
    def reduce_balance(self, date):
        while date != dt.date.today():
            self.balance -= self.balance * 0.005
            date += dt.timedelta(days=1)

    def get_balance(self):
        return self.balance

    def get_withdrawals(self):
        return self.withdraw

    def get_deposits(self):
        return self.deposits

    def get_withdraw_count(self):
        return self.withdraw_count

    def get_withdraw_limit(self):
        return self.withdraw_limit

    def get_withdraw_fee(self):
        return self.withdraw_fee

    def get_limit(self):
        return self.limit

    def set_withdraw_count(self, count):
        self.withdraw_count = count

    def set_withdraw_limit(self, limit):
        self.withdraw_limit = limit

    def set_withdraw_fee(self, fee):
        self.withdraw_fee = fee

    def set_limit(self, limit):
        self.limit = limit

    def reset_withdraw_count(self):
        self.withdraw_count = 0

    def reset_withdraw_limit(self):
        self.withdraw_limit = 4

    def reset_withdraw_fee(self):
        self.withdraw_fee = 5

    def reset_limit(self):
        self.limit = 4

    def reset_balance(self):
        self.balance = 0

    def reset_withdrawals(self):
        self.withdraw = []

    def reset_deposits(self):
        self.deposits = []

    def reset_all(self):
        self.reset_balance()
        self.reset_withdrawals()
        self.reset_deposits()
        self.reset_withdraw_count()
        self.reset_withdraw_limit()
        self.reset_withdraw_fee()
        self.reset_limit()

    def print_balance(self):
        print("Your current balance is: " + str(self.balance))

    def print_withdrawals(self):
        print("Your withdrawals are: " + str(self.withdraw))

    def print_deposits(self):
        print("Your deposits are: " + str(self.deposits))

    def print_withdraw_count(self):
        print("Your withdraw count is: " + str(self.withdraw_count))

    def print_withdraw_limit(self):
        print("Your withdraw limit is: " + str(self.withdraw_limit))

    def print_withdraw_fee(self):
        print("Your withdraw fee is: " + str(self.withdraw_fee))

    def print_limit(self):
        print("Your limit is: " + str(self.limit))

    def print_all(self):
        print("Your current balance is: " + str(self.balance))
        print("Your withdrawals are: " + str(self.withdraw))
        print("Your deposits are: " + str(self.deposits))
        print("Your withdraw count is: " + str(self.withdraw_count))
        print("Your withdraw limit is: " + str(self.withdraw_limit))
        print("Your withdraw fee is: " + str(self.withdraw_fee))
        print("Your limit is: " + str(self.limit))



    
# Create clock object
class Clock:
    # initialize clock object with current date. Keep track of the date of last access.
    def __init__(self):
        self.date = dt.datetime.now()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.last_access = self.date

    # reduce the balance by %0.005 every day until the current date is reached
    def reduce_balance(self, bank):
        bank.reduce_balance(self.date)
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.last_access = self.date


    def save(bank):
        with open("canary_save.pkl", "wb") as f:
            pickle.dump(bank, f)
        
    def load():
        with open("canary_save.pkl", "rb") as f:
            bank = pickle.load(f)
        return bank

    def get_date(self):
        return self.date

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year




# Create objectives object that include: list of daily and repeatable objectives that reward the bank with balance
class Objectives:
    def __init__(self):
        self.daily = ["Floss","30-minute exercise","Brush Teeth","Productive Labor","Small Deed"]
        self.repeatable = ["Study per Logged hour", "Kaggle Work per Logged hour", "Coding per Logged hour", "Zander Time per estimated hour", "Hayley Time per estimated hour"]
        # respective rewards for each objective
        self.daily_rewards = [5, 5, 1, 1, 0.5]
        self.repeatable_rewards = [4, 2, 1, 1, 1]

    def add_daily(self, objective):
        # max 5 objectivates
        if len(self.daily) < 5:
            self.daily.append(objective)
        else:
            print("You have reached your daily objective limit. You cannot add anymore.\nDelete some.")

    def add_repeatable(self, objective):
        # max 5 objectivates
        if len(self.repeatable) < 5:
            self.repeatable.append(objective)
        else:
            print("You have reached your repeatable objective limit. You cannot add anymore.\nDelete some.")

    def get_daily(self):
        return self.daily

    def get_repeatable(self):
        return self.repeatable

    def print_daily(self):
        print("Your daily objectives are: " + str(self.daily))

    def print_repeatable(self):
        print("Your repeatable objectives are: " + str(self.repeatable))

    def print_all(self): 
        print("Your daily objectives are: ")
        for objective in self.daily:
            print(" - " + str(objective) + ": $" + str(self.daily_rewards[self.daily.index(objective)]))
        print("Your repeatable objectives are: ")
        for objective in self.repeatable:
            print(" - " + str(objective) + ": $" + str(self.repeatable_rewards[self.repeatable.index(objective)]))


    def reset_daily(self):
        self.daily = []

   # set daily and repeatable to default values
    def set_default(self):
        self.daily = ["Floss","30-minute exercise","Brush Teeth","Productive Labor","Small Deed"]
        self.repeatable = ["Study per Logged hour", "Kaggle Work per Logged hour", "Coding per Logged hour", "Zander Time per estimated hour", "Hayley Time per estimated hour"]

    def reset_repeatable(self):
        self.repeatable = []

    def reset_all(self):
        self.reset_daily()
        self.reset_repeatable()

    # Complete an objective, increasing the bank balance by an ammount associated with the objective
    def complete_objective(self, bank, objective):
        if objective in self.daily:
            bank.balance += self.daily_rewards[self.daily.index(objective)]
            self.daily.remove(objective)
        elif objective in self.repeatable:
            bank.balance += self.repeatable_rewards[self.repeatable.index(objective)]
        else:
            print("ERROR: You do not have this objective.")

# initialize all objects

# Main method
def main():
    quit = False
    bank = Bank()
    clock = Clock()
    objectives = Objectives()

    try:
        with open('canary_save.pkl', 'rb') as f:
            bank = pickle.load(f)
            clock = pickle.load(f)
            objectives = pickle.load(f)
    except FileNotFoundError: 
        bank = Bank()
        clock = Clock()
        objectives = Objectives()
        with open('canary_save.pkl', 'wb') as f:
            pickle.dump(bank, f)
            pickle.dump(clock, f)
            pickle.dump(objectives, f)
    
    print("Your current balance is: " + str(bank.balance))
    # Main loop
    while True:
        if quit == True:
            break
        # If the current date is different from the clock.last _ccessed, reduce the balance. Reset the objectives list to defaults
        if clock.get_date() != clock.last_access:
            clock.reduce_balance(bank)
            objectives.reset_all()
            clock.last_access = clock.get_date()
            objectives.set_default()
            clock.save(bank)
            clock.save(clock)
            clock.save(objectives)
        
        print("1. Review Objectives")
        print("2. Complete an Objective")
        print("3. Advanced Settings")
        print("4. Withdraw")
        print("5. Quit")
        print("\n")

    # Get user input and perform the corresponding action
        choice = input("What would you like to do? ")
        if choice == "1":
            objectives.print_all()
        elif choice == "2":
            objective = input("What would you like to complete? ")
            objectives.complete_objective(bank, objective)
            print("Your new balance is: " + str(bank.balance))
            # save
            with open('canary_save.pkl', 'wb') as f:
                pickle.dump(bank, f)
                pickle.dump(clock, f)
                pickle.dump(objectives, f)
                # elif specific getter
        elif choice == "getdate":
            print(clock.get_date())
        elif choice == "getbalance":
            print(bank.balance)
        elif choice == "getdaily":
            objectives.print_daily()
        elif choice == "getrepeatable":
            objectives.print_repeatable()
        elif choice == "getobjectives":
            objectives.print_all()
        elif choice == "getlastaccess":
            print(clock.last_access)
        elif choice == "b":
            print(bank.balance)
        elif choice == "quit" or choice == "5":
            quit = True
            break
        elif choice == "3":
            print("1. Add Daily Objective")
            print("2. Add Repeatable Objective")
            print("3. Reset Daily Objectives")
            print("4. Reset Repeatable Objectives")
            print("5. Reset All Objectives")
            print("6. Back")
            print("\n")
            choice = input("What would you like to do? ")
            if choice == "1":
                objective = input("What would you like to add? ")
                objectives.add_daily(objective)
            elif choice == "2":
                objective = input("What would you like to add? ")
                objectives.add_repeatable(objective)
            elif choice == "3":
                objectives.reset_daily()
            elif choice == "4":
                objectives.reset_repeatable()
            elif choice == "5":
                objectives.reset_all()
            elif choice == "6":
                pass
            elif choice == "resetsave":
                bank = Bank()
                clock = Clock()
                objectives = Objectives()
                with open('canary_save.pkl', 'wb') as f:
                    pickle.dump(bank, f)
                    pickle.dump(clock, f)
                    pickle.dump(objectives, f)
                    print("Save file has been reset.")
            else:
                print("ERROR: Invalid input.")
        elif choice == "4":
            withdraw = float(input("How much would you like to withdraw? "))
            bank.withdrawel(withdraw)
            print("Your new balance is: " + str(bank.balance))
            # save
            with open('canary_save.pkl', 'wb') as f:
                pickle.dump(bank, f)
                pickle.dump(clock, f)
                pickle.dump(objectives, f)
        else:
            print("ERROR: Invalid input.")
        print("\n")

    # auto save
        with open('canary_save.pkl', 'wb') as f:
            pickle.dump(bank, f)
            pickle.dump(clock, f)
            pickle.dump(objectives, f)
        
        # sleep for 1 second
        t.sleep(3)



# Run the main method.
main()