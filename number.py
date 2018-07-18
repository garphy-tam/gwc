from random import randint
num = randint(0,10)

answer = input("Guess the number: ")

count=0

while(count < 4):
    count += 1
    if (int(answer) < num):
        answer = input ("Guess a higher number: ")
    if (int(answer) > num):
        answer = input ("Guess a lower number: ")
    if (int(answer)==num):
        print("Correct!")
    if (count==4):
        print ("Better luck next time.")
        break
