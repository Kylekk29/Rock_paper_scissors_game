import tkinter as tk
import random

def showresult(result,computer_choice_showresult):
    computer_choice_label_0 = tk.Label(text='computer choice:', font=('Arial', 30))
    computer_choice_label_1 = tk.Label(text=computer_choice_showresult, font=('Arial', 30))
    result_label = tk.Label(text=result, font=('Arial', 30))
    result_label.config(bg='black')
    result_label.config(fg='white')
    result_label.place(x=0,y=150,width=150,height=100)
    computer_choice_label_0.config(bg='skyblue')
    computer_choice_label_1.config(bg='skyblue')
    computer_choice_label_0.place(x=0,y=150,width=300,height=250)
    computer_choice_label_1.place(x=300,y=150,width=150,height=250)


def main1(player_choice):
    global determineresult
    if player_choice == computer_choice:
        determineresult = 'Tie'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        determineresult = 'Win'
    elif player_choice == 'rock' and computer_choice == 'paper':
        determineresult = 'Lose'
    elif player_choice == 'paper' and computer_choice == 'rock':
        determineresult = 'Win'
    elif player_choice == 'paper' and computer_choice == 'scissors':
        determineresult = 'Lose'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        determineresult = 'Win'
    elif player_choice == 'scissors' and computer_choice == 'rock':
        determineresult = 'Lose'
    showresult(determineresult,computer_choice)


   


def main():
        global computer_choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        rock_btn = tk.Button(window, text='Rock',font=('Arial',30) ,command=lambda: main1('rock'))
        paper_btn =tk.Button(window, text='Paper',font=('Arial',30) ,command= lambda: main1('paper'))
        scissors_btn = tk.Button(window,text='Scissors',font=('Arial',30) ,command =lambda: main1('scissors'))
        rock_btn.place(x=0, y=0,width=200,height=100)
        paper_btn.place(x=200, y=0,width=200,height=100)
        scissors_btn.place(x=400, y=0,width=200,height=100)
        rock_btn.config(bg='red')
        paper_btn.config(bg='green')
        scissors_btn.config(bg='yellow')
        window.mainloop()
window = tk.Tk()
window.geometry('600x500')
window.resizable(False, False)
window.title('Rock Paper Scissors')
window.config(bg='skyblue')
main()