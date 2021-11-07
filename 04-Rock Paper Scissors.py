"""A generic rock paper scissors game"""

import random

print("Welcome to Rock Paper Scissors \n \n")

print("Enter Your Choice : \n\
'r' for Rock , \n\
'p' for Paper and \n\
's' for scissors")

user = input("Enter your choice : ")
computer = random.choice(['r' , 'p' , 's'])

if(user == computer):
    print("It's a Tie!")

elif ((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or\
(user == 's' and computer == 'p')):
    print("Yaay ! You Won.")
    
elif (user == 'r' and computer == 'p' or (user == 'p' and computer == 's') or \
(user == 's' and computer == 'r')):
    print("Alas ! You Lost.")  

else:
    print("Wrong Input. Input only 'r' , 'p' or 's'")