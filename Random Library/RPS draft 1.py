import random

name=input("What is your name")

choices=["rock", "paper","scissors"]


print("Welcome" + name)
user_choice= input("Choose between rock, paper and scissors")

#List can have numbers or words
computer_choice=random.choice(choices)
print("User chose: " + computer_choice)
print("Computer chose: " + user_choice)

if user_choice==computer_choice:
    print("it's tie!")
    
if user_choice=="rock" and computer_choice=="scissors":
    print("Player Wins")   
    
if user_choice=="paper" and computer_choice=="rock":
    print("Player Wins")   
    
if user_choice=="scissors" and computer_choice=="paper":
    print("Player Wins")  
else:
    print("User Loses")