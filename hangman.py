from random import random

import random
from tkinter import *
from tkinter import messagebox

import c1

score = 0
run = True

# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg='#E7FFFF')
    count = 0
    win_count = 0
    max_chances = 6

    # Read words and hints from file
    with open('word.txt', 'r') as file:
        lines = file.readlines()

    # Ensure the list has enough entries and choose a word
    if len(lines) > 0:
        index = random.randint(0, len(lines) - 1)
        line = lines[index].strip('\n')
        if ',' in line:
            selected_word, hint = line.split(',', 1)
        else:
            selected_word, hint = "example", "Default hint"  # Fallback in case of format issues

    # Debugging prints to check if the hint is being read correctly
    print(f"Selected Word: {selected_word}")
    print(f"Hint: {hint}")

    # Creation of word dashes variables
    x = 250
    for i in range(len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i, x, 450))

    # Display the hint
    hint_label = Label(root, text="Hint: " + hint, bg="#E7FFFF", font=("arial", 20))
    hint_label.place(x=250, y=100)

    # Display remaining chances
    remaining_chances_label = Label(root, text="Remaining Chances: " + str(max_chances - count), bg="#E7FFFF", font=("arial", 20))
    remaining_chances_label.place(x=250, y=150)

    # Letters icon
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let, let))

    # Hangman images
    h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman, hangman))

    # Letters placement
    button = [['b1', 'a', 0, 595], ['b2', 'b', 70, 595], ['b3', 'c', 140, 595], ['b4', 'd', 210, 595],
              ['b5', 'e', 280, 595], ['b6', 'f', 350, 595], ['b7', 'g', 420, 595], ['b8', 'h', 490, 595],
              ['b9', 'i', 560, 595], ['b10', 'j', 630, 595], ['b11', 'k', 700, 595], ['b12', 'l', 770, 595],
              ['b13', 'm', 840, 595], ['b14', 'n', 0, 645], ['b15', 'o', 70, 645], ['b16', 'p', 140, 645],
              ['b17', 'q', 210, 645], ['b18', 'r', 280, 645], ['b19', 's', 350, 645], ['b20', 't', 420, 645],
              ['b21', 'u', 490, 645], ['b22', 'v', 560, 645], ['b23', 'w', 630, 645], ['b24', 'x', 700, 645],
              ['b25', 'y', 770, 645], ['b26', 'z', 840, 645]]

    for q1 in button:
        exec(
            '{}=Button(root,bd=0,command=lambda let=q1[1], btn=q1[0]: check(let,btn),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(
                q1[0], q1[1], q1[0], q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

    # Hangman placement
    han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0], p1[1]))

    # Placement of first hangman image
    c1.place(x=900, y=90)

    # Exit button
    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer:
            run = False
            root.destroy()

    e1 = PhotoImage(file='exit.png')
    ex = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=e1)
    ex.place(x=1410, y=10)
    s2 = 'SCORE:' + str(score)
    s1 = Label(root, text=s2, bg="#E7FFFF", font=("arial", 25))
    s1.place(x=10, y=10)

    # Button press check function
    def check(letter, button):
        global count, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER', 'YOU WON!\nWANT TO PLAY AGAIN?')
                if answer:
                    run = True
                    root.destroy()
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count + 1, 800, 90))
            remaining_chances_label.config(text="Remaining Chances: " + str(max_chances - count))
            if count == max_chances:
                answer = messagebox.askyesno('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()

    root.mainloop()