from tkinter import *
import random

# Score variables
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# Function to play
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice : " + user_choice)
    computer_label.config(text="Computer Choice : " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Your Score : {user_score}    Computer Score : {computer_score}"
    )

# Reset Game
def reset():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="Your Choice :")
    computer_label.config(text="Computer Choice :")
    result_label.config(text="")
    score_label.config(text="Your Score : 0    Computer Score : 0")


# Main Window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")

Label(root, text="Rock Paper Scissors",
      font=("Arial", 18, "bold")).pack(pady=10)

Button(root, text="Rock", width=15,
       command=lambda: play("Rock")).pack(pady=5)

Button(root, text="Paper", width=15,
       command=lambda: play("Paper")).pack(pady=5)

Button(root, text="Scissors", width=15,
       command=lambda: play("Scissors")).pack(pady=5)

user_label = Label(root, text="Your Choice :", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = Label(root, text="Computer Choice :", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = Label(root, text="Your Score : 0    Computer Score : 0",
                    font=("Arial", 12))
score_label.pack(pady=10)

Button(root, text="Reset Game", width=15,
       command=reset).pack(pady=10)

root.mainloop()
