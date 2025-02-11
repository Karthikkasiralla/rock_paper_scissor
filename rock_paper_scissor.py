import  random
rock =('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

''')
scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
computer_choice = random.randint(0,2)
images =[rock,paper,scissor]
user_choice = int(input('Enter a number 0 for "Rock", 1 for "Paper", and 2 for "Scissors"\n'))

if not 0 <= user_choice <= 2:
    print("You entered an invalid number 😒, you lost the game !!!")
else:
    # Display user's choice
    print("You chose:")
    print(images[user_choice])

    # Computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[computer_choice])

#logic to find who wins the game

    if user_choice == computer_choice:
        print("Match Draw 🤝")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win 🎉🎊")
    else:
        print("You Lose 😞")