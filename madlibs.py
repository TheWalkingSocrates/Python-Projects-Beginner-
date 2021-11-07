#Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price.\
#It consistsof one player prompting others for a list of words to substitute for blanks in a story before reading aloud.\
#The game is frequently played as a party game or as a pastime.

person = input("Enter if it's a Guy/Girl/Non Binary: ")
name = input("Enter Name: ")
subject = input("Enter The Subject: ")
company = input("Enter The Company: ")
position =input("Enter The Position: ")

chomu = person.lower()
if(chomu== 'guy'):
    gender = "He"
elif(chomu == 'girl'):
    gender = 'she'
else:
    gender = 'They'



print(f"There was once a {person} whose name was {name}. {gender} was poor but highly motivated person.\
{gender} thought \"I'll not be poor my entire life.\" So {name} started studying {subject} since\
{gender} liked the subject and worked hard, day and night. One day the hard work paid off and {gender}\
got a job at {company} as a {position}. {gender} cried at that moment. {name},{position} looked really\
good on the plaque. Hard Work Pays Off :) ")