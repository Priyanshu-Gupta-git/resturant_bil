import datetime
import emoji
now = datetime.datetime.now()
menu = {
    'PIZZA': 160,
    'PASTA': 50,
    'BURGER': 40,
    'CHOMINE': 50,
    'COFFEE': 40,
    'MOMOS': 50,
    'TEA': 20,
    'SANDWITCH': 100,
    'CHOCOLATE': 150,
    'ICECREAM': 90,
    
    
}

print(" ".rjust(20),"\033[1;103;31m \U0001F60B Welcome to my Restaurant\033[0m")
print("\033[1;93;46mHere's our menu:\n")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
print("\n")
for i in range(1,7):
    for j in range(1,6):
        print("--",end=":")
order_total = 0
while True:
    item = input("Enter the name of the item you want to order or (type 'exit' to finish ):").upper()
    
    if item == 'EXIT':
        break
    elif item in menu:
        order_total += menu[item]
        print(f"\033[103mYour item {item} has been added to your order. Current total:₹{order_total}\033[0m")
    else:
        print(f"\033[1;103mSorry, {item} is not  available yet.\033[0m")

for i in range(1,7):
    for j in range(1,6):
        print("--",end=":")
    
print(f"\n\033[46Your final order total Amount is: ₹{order_total}. Thank you for dining with us!\033[0m")
print(now.strftime("\033[1;91;103m Date  %d-%B-%Y \n  Time %H:%M:%S \\ Day- %A\033[0m"))
for i in range(1,7):
    for j in range (1,6):
        print("--",end=":")
        
        
        