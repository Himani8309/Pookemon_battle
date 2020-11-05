from time import sleep

def password():
    pin = int(input("Please Enter your Account pin:"))
    if pin == 6297:
        print("Correct Account, Please wait we are fetching youe data")
        return True
    else:
        print("Incorrect passwoord, athentication failed!!")
        return False

def atm_start():

    balance = 0

    print("Hello , Welcome to the AARUSH ATM")
    if password():
        while True:
            print("Press '1' for checking Balance")
            print("Press '2' for withdrawl")
            print("Press '3' for deposit")
            print("Press '4' for exiting out of the ATM")

            choose = int(input("\nChoose which money transaction fits for your day:"))

            if choose == 1:
                print("Please wait we are fetching your data...")
                sleep(2)
                print("Your account balance is: ",balance)

            elif choose == 2:
                print("Please wait we are fetching your data...")
                sleep(2)
                withdrawl = int(input("\nHow much money do you want to take from your account:"))
                balance = balance - withdrawl
                print(f"You have successfully taken {withdrawl} money from your account")

            elif choose == 3:
                print("Please wait we are fetching your data...")
                sleep(2)
                deposit = int(input("\n How much money do you want to add to your account:"))
                balance = balance + deposit
                print(f"You have successfully added {deposit} money in your account")

            elif choose == 4:
                print("Please wait we are fetching your data...")
                sleep(2)
                print("Thanks for using the ATM, Hope you have a good day!!")
                break

atm_start()
