# Program to check 1 Dice thrown simulation

import random

flag = "y"
   
while flag == "y":
    number = random.randint(1,6)
      
    if number == 1:
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    if number == 2:
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    if number == 3:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    if number == 4:
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    if number == 5:
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    if number == 6:
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
          
    flag = input("press y to roll again and n to exit:")
    print("\n ======= ")
