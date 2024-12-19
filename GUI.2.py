import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.secret_number = random.randint(1, 10)
        
        self.label = tk.Label(master, text="Guess a number between 1 and 10:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 10:
                messagebox.showerror("Error", "Please guess a number between 1 and 10.")
                return
            
            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", "Yeah, you guessed it!")
                self.play_again_button.config(state=tk.NORMAL)
                self.guess_button.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("Try Again", "Wrong guess! Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def play_again(self):
        self.secret_number = random.randint(1, 10)
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)


root = tk.Tk()
game = GuessingGame(root)

root.mainloop()