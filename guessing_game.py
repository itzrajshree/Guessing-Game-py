import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.background_image=tk.PhotoImage(file="background.png")
        canvas = tk.Canvas(self.root, width=700, height=200)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.root.configure(bg="lightpink")
        self.random_number = random.randint(1, 20)
        

        self.label = tk.Label(self.root, text="Welcome to the guessing game!\nComputer has guessed a value between 1 to 20\nNow is your turn to guess!",bg="lightblue")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(self.root, text="Take your Guess", command=self.check_guess,bg='maroon',fg='white')
        self.guess_button.pack(pady=20)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess > self.random_number:
                messagebox.showinfo("Result", "Too high! Try again!")
            elif guess < self.random_number:
                messagebox.showinfo("Result", "Too low! Try again!")
            else:
                messagebox.showinfo("Result", f"Hooray! You got the guess right, the number was: {guess}")
                self.root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessingGame()
    game.run()
