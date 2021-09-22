import random
import time
lst=['rock','paper','scissor']
user_score=0
pc_score=0
for i in range(1,4):
    print(f"{i} of 3 try")
    user_choice=input("enter the choice: ")
    choice=random.choice(lst)
    print(f"pc choice is {choice}")
    if user_choice==choice:
        print('draw')
    elif user_choice=='rock' and choice=='scissor':
        print('user wins')
        user_score+=1
    elif user_choice=='paper' and choice=='rock':
        print('user wins')
        user_score+=1
    elif user_choice=='scissor' and choice=='paper':
        print('user wins')
        user_score+=1
    else:
        print('pc wins')
        pc_score+=1
    time.sleep(2)
print("\n\n\nfinal result\n")
if user_score > pc_score:
    print("u win!!!!")
elif user_score==pc_score:
    print("drawwwwwwwwwww")
else:
    print("loserrrr!!!!!!!")

