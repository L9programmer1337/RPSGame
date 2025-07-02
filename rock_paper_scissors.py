import random
import time

game = True
count = 0
win = 0
lose = 0
draw = 0

while game:
    
    try:
        yourchose = int(input(f"1. Rock, 2. Paper, 3. Scissors? (Games played: {count}) "))
        
    except ValueError:
        print("It's not a number!")
        continue
    
    bot = random.randrange(1,4)
    
    if bot == 1 and yourchose == 2:
        win = win + 1
        print("You won!")
        
    elif bot == 1 and yourchose == 3:
        lose = lose + 1
        print("You've lost!")
        
    elif bot == 1 and yourchose == 1:
        draw = draw + 1
        print("Draw!")
        
    elif bot == 2 and yourchose == 3:
        win = win + 1
        print("You won!")
        
    elif bot == 2 and yourchose == 1:
        lose = lose + 1
        print("You've lost!")
        
    elif bot == 2 and yourchose == 2:
        draw = draw + 1
        print("Draw!")
        
    elif bot == 3 and yourchose == 1:
        win = win + 1
        print("You won!")
        
    elif bot == 3 and yourchose == 2:
        lose = lose + 1
        print("You've lost")
        
    elif bot == 3 and yourchose == 3:
        draw = draw + 1
        print("Draw!")
        
    while yourchose < 1 or yourchose > 3:
        
        try:
            yourchose = int(input("Choose a number between 1 and 3! "))
            
            if yourchose == 1 or yourchose == 2 or yourchose == 3:
                count = count - 1
            
        except ValueError:
            print("It's not a number!")
            continue
        
    count = count + 1
    
    gaming = input("Would you like to continue? (Y/N) ")
    
    while gaming != "Y" and gaming != "N" and gaming != "y" and gaming !="n":
        gaming = input("Would you like to continue? (Y/N) ")
        
    if gaming == "Y" or gaming == "y":
        pass
    
    elif gaming == "N" or gaming == "n":
        game = False
        winrate = (win / count) * 100
        print("Thanks for playing!")
        print(f"Games: {count}\nWin rate: ",round(winrate, 1),f"%\nWins: {win}\nLoses: {lose}\nDraws: {draw}")
        time.sleep(5)
        print("Quitting...")
        time.sleep(1)
        pass