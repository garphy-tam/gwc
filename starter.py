def main():
    while(True):
        choice = input("\nPress 1 to hear a joke, 2 to see a poem, 3 to hear a pun, 4 to play rock paper scissor, 5 to roll a dice, 6 to find out what you should eat for dinner, 7 to exit")
        if choice == "1":
            joke()
        elif choice == "2":
            poem()
        elif choice =="3":
            pun()
        elif choice =="4":
            rockPaperScissor()
        elif choice=="5":
            dice()
        elif choice=="6":
            dinner()
        elif choice =="7":
            print("Bye, see you next time!")
            exit()

def poem():
    print("\nTime spent in nature")
    print("is time spent realizing")
    print("that you don't know it all")
    print("and that you never will\n")

def joke():
    print("\nWhy was 6 afraid of 7?")
    print("Because 789\n")

def pun():
    print("\nYou are egg-cellent!\n")

def rockPaperScissor():
    answer = input("Rock, paper, or scissor?")
    if answer == "rock":
        print ("\nYou lost.\n")
    elif answer == "scissor":
        print("\nYou won.\n")
    elif answer == ("paper"):
        print("\nIt's a tie.\n")

def dinner():
    import random
    list_sides = ["soup", "fries", "mashed potato"]
    list_main = ["chicken", "salmon", "salad"]
    list_dessert = ["cookies", "pudding", "chocolate shortcake"]
    print(random.choice(list_sides))
    print(random.choice(list_main))
    print(random.choice(list_dessert))


def dice():
    from random import randint
    num_1 = randint(1,6)
    print("\nYou got",num_1)


print("Hello")
main()
