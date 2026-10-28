#Number Guessing Game 

#importing module random
import random as rd

#Wlecoming
name = input("What can i call you my friend ?\n")
print(f"Hiiii {name}\nWlecome In Our Number Guessing Game :)")

#logic gates
random_number = rd.randint(1,11)
tries = 0
while True:
    guess = int(input(f"{name} Guess A Number Between (1 To 10) ?\n"))
    if  random_number == guess:
         tries += 1
         print(f"You guessed it right {name} yeaahhh\nYou guessed right number in {tries} tries")
         break
    elif random_number < guess:
         tries += 1
         print(f"Go a littel lower {name}")
    elif random_number > guess:
         tries += 1
         print(f"GO a littel higher {name}")
    else:
         tries += 1
         print(f"OOH No {name} it's wrong but no worreis try it again ")

#Want to quit game 
ask = input("Do you want to end the game (yes/no) ?/n")
if ask == yes:
     print(f"Okkkeiie {name} have nice day")
else:
     print(f"okkekie let's play one more time {name}") 
