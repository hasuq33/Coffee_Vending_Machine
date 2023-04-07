MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def update():
   water1 = int(input("Enter the amount of water:"))
   milk2 = int(input("Enter the amount of milk:"))
   coffee3 = int(input("Enter the amount of coffee in gm:"))
   resources["water"] = resources["water"] + water1
   resources['milk']= resources['milk'] + milk2
   resources["coffee"] = resources["coffee"] + coffee3

def serve(money):
  if money >= 1.5 and money <2.5:
    print("You shoud go with expresso")
    print("The price of Expresso is $1.5 for full glass.")

  elif money >=2.5 and money<3.0:
    print("You can go with both expresso and Latte! ") 
    print("The price of Latte is $2.5 for for full glass.")  
    print("The price of Expresso is $1.5 for full glass.")
  
  elif money >= 3.0:
    print("You can choose anyone of them.")

  else:
    print("Go back get more money and otherwise don't come here!")  

# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

while True:
  water =resources["water"]  
  milk = resources['milk']
  coffee = resources["coffee"]
  
  if water<=0 or milk<= 0 or coffee <= 0:
    usr = input("Enter 'y' for entering resources or 'q' for stop running the program.").lower()
    if usr== 'y':
      update()
    elif usr == 'q':
      break
    else:
      print("Invalid input!")
  
  print(f"We have {water}ml water, {milk}ml milk and {coffee}gm coffee.")
  print("Enter thr coins.")
  
  quarters = int(input("quarters: "))
  dimes = int(input("dimes: "))
  nickles = int(input("nickles: "))
  pennies = int(input("pennies: "))
  money = (quarters*.25) + (dimes*.10) + (nickles*.05) + (pennies*.01) #Calculating total money
  if money < 0:
    print("Enter the positive number in coin")
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))
    money = (quarters*.25) + (dimes*.10) + (nickles*.05) + (pennies*.01)
    money = round(money,2)
    
  print(money)

  serve(money) #This function suggest you base on what item you should order
  if money < 1.5:
    money = serve(money)
  
  user = input("What would you like to serve? 'Latte' ,'Expresso' or 'Cappacino'? or are you a admin? ").lower()

  if user == 'latte':
    print("Here is your latte")
    resources["water"] = resources["water"] - 200
    resources['milk']= resources['milk'] - 150
    resources["coffee"] = resources["coffee"] - 24     

  elif user == 'expresso':
    print("Here is your expresso")
    resources["water"] = resources["water"] - 50
    resources["coffee"] = resources["coffee"] - 18

  elif user== 'cappacino':
    print("Here is your cappacino")
    resources["water"] = resources["water"] - 250
    resources['milk']= resources['milk'] - 100
    resources["coffee"] = resources["coffee"] - 24

  elif user == 'admin':
    update()
      
  else:
    print("This is the invalid input. enter 'q' for quit")
    if user == 'q':
      break






