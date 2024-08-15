import time

print("Insert your Debit CARD")

time.sleep(0.02)

password=3011

pin=int(input("Enter your four digit pin = "))



balance = 20000

if pin==password:
    while True:
        print(""" ----------- Menu----------- """"")
        print("1 == balance")
        print("2 == withdraw balance")
        print("3 == deposit balance")
        print( "4 == exit")
            
            
        try:
            option=int(input("Enter your choice = "))
        except:
            print("Enter valid option = ")
            
        if option == 1:
            print(f"Your current balance is {balance} ")
            
            print("-------------------------------------------------------")
            print("-------------------------------------------------------")
            
        if option == 2:
            
            withdraw_amount=int(input("Enter withdraw_amount = "))
            
            balance = balance-withdraw_amount
            print("-------------------------------------------------------")
            print("-------------------------------------------------------")
            
            print(f"{withdraw_amount} is debited from your account  ")
            print("-------------------------------------------------------")
            print("-------------------------------------------------------")
            
            print(f"your current balance is {balance} ")
            print("-------------------------------------------------------")
            
            
            
        if  option == 3:
            
            deposit_amount = int(input("Enter deposit_amount = "))
            
            balance = balance+deposit_amount
            print("-------------------------------------------------------")
            
            print(f"{deposit_amount} is credited to your account ")
            print("===========================================================")
            
            print(f"your updated balance is {balance} ")
            print("===========================================================")
            
        if option == 4:
            print("===========================================================")
            break                

else:
    print("Incorrect Pin!! Try again")