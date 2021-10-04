import random 
print("welcome to my game rock,scissors or paper ")
print(sep="\n")
rock='''
        _____
.......|    ___)
           (___)  
           (___)  rock
           (___)
-------_(____) 

'''
scissors='''
       _____
......|    ___)__
                  ___)__
                  ____) scissors
             (____)
......|      (___)


       
'''
paper='''
       _____
......|    ___)__
                  ___)__
                  ____) paper
                  ____)
......|    ___)


'''
game=[rock,scissors,paper]
you_win=0
computer_win=0
draw_game=0
print("this is the three(3) rounded game if u want to win you should win two(2) time")
while (1):
    for i in range (1,4):
        print("------------------------------------------------------round",i,"start---------------------------------------")
        print(sep="\n")
        your_choice=str(input("please enter rock , scissors or paper -->  "))
#         print("your choice is--> ",your_choice)
        if your_choice=="rock":
            your_choice=rock
            print("your choice is--> ",rock)
        elif your_choice=='scissors':
            your_choice=scissors
            print("your choice is--> ",scissors)
        elif your_choice=='paper':
            your_choice=paper
            print("your choice is--> ",paper)
        else:
            print("invalid input")
        computer_choice=random.choice(game)
        print("the computer choice is--> ",computer_choice)
        if your_choice==computer_choice:
            draw_game+=1
            print("draw the game")
        elif (your_choice==paper and computer_choice==rock or your_choice==scissors and computer_choice==paper or your_choice==rock and computer_choice==scissors):
            you_win+=1
            print("you win")
        elif (your_choice==rock and computer_choice==paper or your_choice==scissors and computer_choice==rock or your_choice==paper and computer_choice==scissors):
            computer_win+=1
            print("you lose")
        else:
            print(" your choice is invalid and the remaining results are below ")
            break
    print(sep="\n")
    print("-----------------------------------------------------THE RESULTS ARE---------------------------------------")
    print("you win ",you_win," time")
    print("computer win ",computer_win," time")
    print("the game draw",draw_game,"time")
    print("-----------------------------------------------------THE FINAL RESULTS IS----------------------------------")
    if you_win==computer_win:
        print("at the result the game is draw")
    elif you_win>computer_win:
        print("at the result you win")
    else:
        print("at the result computer win")
    user_choice=input("enter yes to to continue and no to terminate ")
    print(sep="\n")
    if user_choice=='Yes'or  user_choice=='yes' or  user_choice=='YES':
        print("------------------------------------------------------THE GAME AGAIN START----------------------------------")
        print(sep='\n')
        print(sep='\n')
        continue
    elif user_choice=='No'or  user_choice=='no' or  user_choice=='NO':
        print("--------------------------------------------------------GAME OVER------------------------------------------")
        break