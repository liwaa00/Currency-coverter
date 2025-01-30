import os
import time
def clear():
    os.system("cls" if os.name=="nt" else "clear")
currency={
"USD":1.0,
"EUR":0.85,
"EGP":30.9,
"RMB":6.5,
}
def money(convert_from,convert_to,amount):
        
    answer=currency[convert_to]/currency[convert_from]
    print(f"Exhange Rate : 1 {convert_from} = {answer:.2f} {convert_to}  \n")
    time.sleep(4)
    print(f"{amount} {convert_from} is equal to {answer*amount:.2f} {convert_to}\n")

def display():
    clear()
    print("""
  _ __ ___   ___  _ __   ___ _   _ 
 | '_ ` _ \ / _ \| '_ \ / _ \ | | |
 | | | | | | (_) | | | |  __/ |_| |
 |_| |_| |_|\___/|_| |_|\___|\__, |
                             |___/ """)
    
    for i in currency:
        print(f"{i}: {currency[i]}\n")
    convert_from=input("Choose a currency  to convert from :").upper()# يتحول من اي عملة
    while True:
        amount=float(input("enter the amount :"))#كمية
        confirm=input(f"\nYou entered {amount} {convert_from.upper()}. confirm? (Y/N): ").upper()#تاكيد
        if confirm=="Y":
            break
    clear()
    for i in currency:
        print(f"{i}: {currency[i]}\n")
    convert_to=input("Choose a currency  to convert to :").upper()#الى اي عملة ستحول
    print("Analyzing your request...")
    time.sleep(2)
    print(f"checking for {convert_to}'s best rates available...")
    time.sleep(2)
    print(f"Getting a discount price for {(convert_from)}...\n")
    time.sleep(4)
    if convert_from not in currency or convert_to not in currency:
        print("invalid currency...")
        time.sleep(2)
        display()
    print(f"\npreparating the deal from {convert_from} to {convert_to} ...\n")
    time.sleep(2)
    money(convert_from,convert_to,amount)
    accept=input("Do you accept this transaction? (y/n):\n").upper()
    print("done successfully.") if accept=="Y" else print("transaction canceled.")
    another=input("Do you want to perform another conversion ? (y/n):").upper()
    if another=="Y":
        True
    else:
        print("Exiting...")
    
