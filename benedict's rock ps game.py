from random import choice
from tkinter import *
from tkinter import messagebox as msg

def clear():
    # Clear previous text
    my_text.config(state=NORMAL)
    my_text.delete("1.0", "end")
    my_text.config(state=DISABLED)

def loading(user_choice):
    global loading_steps, user_score, bot_score

    loading_steps = [".", "..", "..."]
    step_loading(user_choice, 0)
    scissors_button['state'] = DISABLED
    paper_button['state'] = DISABLED
    rock_button['state'] = DISABLED    

def step_loading(user_choice, step):
    global loading_steps

    if step < len(loading_steps):
        clear()

        # Display user choice immediately
        my_text.config(state=NORMAL)
        my_text.insert(END, f"\nYOUR SCORE: {user_score}\t\t\tBOT'S SCORE: {bot_score}\n\n")
        my_text.insert(END, f"You chose: {user_choice}\t\t\tBot chose: {loading_steps[step]}")
        my_text.config(state=DISABLED)

        window.after(100, step_loading, user_choice, step + 1)
    else:
        bot_choice(user_choice)

def bot_choice(user_choice):
    global user_score, bot_score

    clear()

    possible_choice = ["rock", "paper", "scissors"]
    computer_choice = choice(possible_choice)


    if user_choice == "rock":
        if computer_choice == "paper":
            bot_score += 1
        elif computer_choice == "scissors":
            user_score += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            bot_score += 1
        elif computer_choice == "rock":
            user_score += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            bot_score += 1
        elif computer_choice == "paper":
            user_score += 1

    my_text.config(state=NORMAL)
    my_text.insert(END, f"\nYOUR SCORE: {user_score}\t\t\tBOT'S SCORE: {bot_score}\n\n")
    my_text.insert(END, f"You chose: {user_choice}\t\t\tBot chose: {computer_choice}")
    my_text.config(state=DISABLED)

    if user_score == 3:
        msg.showinfo("Final Result", f"CONGRATULATIONS!! YOU WON \n{user_score} : {bot_score}")
        play_again = msg.askyesno("Game over", "Would You Like to Play Again")
        window.destroy()
        if play_again:
            main_win()
    
    elif bot_score == 3:
        msg.showinfo("Final Result", f"YOU LOST!! \n{user_score} : {bot_score}")
        play_again = msg.askyesno("Game over", "Would You Like to Play Again")
        window.destroy()
        if play_again:
            main_win()
        
    
    rock_button['state'] = NORMAL
    scissors_button['state'] = NORMAL
    paper_button['state'] = NORMAL

def main_win():
    global user_score, bot_score, my_text, rock_button, paper_button, scissors_button, window
    # Initialize main window

    window = Tk()
    window.minsize(height=400, width=400)
    window.title("Rock Paper Scissors")

    # Define styles
    bg_color = "#f0f0f0"
    button_bg = "#4CAF50"
    button_fg = "#ffffff"
    font_large = ("Arial", 14, "bold")
    font_medium = ("Arial", 12)
    font_small = ("Arial", 10)

    window.config(bg=bg_color)

    # Initialize scores
    user_score = 0
    bot_score = 0

    # Create frames for better organization
    top_frame = Frame(window, bg=bg_color)
    top_frame.pack(pady=10)

    middle_frame = Frame(window, bg=bg_color)
    middle_frame.pack(pady=10)

    bottom_frame = Frame(window, bg=bg_color)
    bottom_frame.pack(pady=10)

    # Add title
    title_label = Label(top_frame, text="Rock Paper Scissors", font=font_large, bg=bg_color)
    title_label.pack()

    # Add instructions
    instruction_label = Label(top_frame, text="Pick one:", font=font_medium, bg=bg_color)
    instruction_label.pack()

    # Add buttons
    rock_button = Button(middle_frame, text="Rock", height=2, width=12, command=lambda: loading("rock"), bg=button_bg, fg=button_fg, font=font_medium)
    rock_button.pack(side=LEFT, padx=10)
    paper_button = Button(middle_frame, text="Paper", height=2, width=12, command=lambda: loading("paper"), bg=button_bg, fg=button_fg, font=font_medium)
    paper_button.pack(side=LEFT, padx=10)
    scissors_button = Button(middle_frame, text="Scissors", height=2, width=12, command=lambda: loading("scissors"), bg=button_bg, fg=button_fg, font=font_medium)
    scissors_button.pack(side=LEFT, padx=10)

    # Add text area to display scores and choices
    my_text = Text(bottom_frame, width=48, height=10, font=font_small, bg="#ffffff", bd=2, relief="solid")
    my_text.pack(pady=10)
    my_text.insert(END, f"\nYOUR SCORE: 0\t\t\tBOT'S SCORE: 0\n\n")
    my_text.insert(END, f"You chose: \t\t\tBot chose: ")
    my_text.config(state=DISABLED)

    window.mainloop()

def introduction():
    intro_win = Tk()
    intro_win.minsize(height=400, width=400)
    intro_win.title("Rock Paper Scissors")

    # Define styles
    bg_color = "#f0f0f0"
    button_bg = "#4CAF50"
    button_fg = "#ffffff"
    font_large = ("Arial", 14, "bold")
    font_medium = ("Arial", 12, "bold")
    font_small = ("Arial", 10)

    intro_win.config(bg=bg_color)

    # Create frames for better organization
    top_frame = Frame(intro_win, bg=bg_color)
    top_frame.pack(pady=10)

    middle_frame = Frame(intro_win, bg=bg_color)
    middle_frame.pack(pady=10)

    bottom_frame = Frame(intro_win, bg=bg_color)
    bottom_frame.pack(pady=10)

    # Add title
    title_label = Label(top_frame, text="Welcome To Rock Paper Scissors", font=font_large, bg=bg_color)
    title_label.pack()
    Label(middle_frame, text="Instructions:", font=font_small, bg=bg_color).pack()
    Label(middle_frame, text="If the player wins the round, they earn one point.\n\nIf the bot wins the round, the bot earns one point.\n\nA tie does not earn any points for either side.",
          font=font_medium, bg=bg_color).pack()
    Label(middle_frame, text="\nThe first to reach three points wins the game.", font=font_large, bg=bg_color).pack()
    Button(bottom_frame, text="PLAY", height=2, width=12, bg=button_bg, fg=button_fg, command=lambda: [intro_win.destroy(), main_win()]).pack()

    intro_win.mainloop()

introduction()
