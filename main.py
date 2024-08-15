import tkinter as tk
import csv
# import threading
import random

class QuizkApp:
    def __init__(self, root, questions_file):
        self.root = root
        self.root.title("Quizk")
        self.root.geometry('700x450')

        # Dark theme colors
        self.bg_color = "#2e2e2e"  # Dark grey background
        self.fg_color = "#ffffff"  # White text
        self.button_bg_color = "#4b4b4b"  # Dark grey for buttons
        self.button_active_bg_color = "#1c1c1c"  # Even darker grey for active buttons
        
        # Set the background color of the root window
        self.root.config(bg=self.bg_color)
        
        # Create and place widgets
        self.create_widgets()

        # Load questions and ask the first question
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.current_question = None
        self.ask_question()

    def create_widgets(self):
        # Question label
        self.label = tk.Label(self.root, text="Are you ready for a question?", bg=self.bg_color, fg=self.fg_color, font=("Arial", 16, "bold"), padx=20, pady=20)
        self.label.pack()

        # Variable for storing the selected answer
        self.answer_var = tk.StringVar()

        # Create radio buttons for answer choices
        self.radio_frame = tk.Frame(self.root, bg=self.bg_color)
        self.radio_frame.pack(pady=10, padx=20, fill=tk.X)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.radio_frame, text="", variable=self.answer_var, value="", bg=self.bg_color, fg=self.fg_color, selectcolor="#6c6c6c", font=("Arial", 14), anchor="w")
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        # Submit button
        self.button = tk.Button(self.root, text="Submit Answer", command=self.check_answer, bg=self.button_bg_color, fg=self.fg_color, font=("Arial", 14, "bold"), activebackground=self.button_active_bg_color)
        self.button.pack(pady=20, padx=20)

        # Result label
        self.result_label = tk.Label(self.root, text="", bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), padx=20, pady=10)
        self.result_label.pack()

    def load_questions(self):
        questions = []
        with open(self.questions_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                questions.append(row)
        return questions

    def ask_question(self):
        self.current_question = random.choice(self.questions)
        self.label.config(text=self.current_question['question'])
        self.answer_var.set(None)

        # Update radio buttons with choices
        for i, choice in enumerate(['choice1', 'choice2', 'choice3', 'choice4']):
            self.radio_buttons[i].config(text=self.current_question[choice], value=self.current_question[choice])
        
        self.result_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_var.get().strip()
        correct_answer = self.current_question['answer'].strip()
        is_correct = user_answer.lower() == correct_answer.lower()

        if is_correct:
            self.result_label.config(text="Correct!", fg="#00ff00")  # Green for correct answer
        else:
            self.result_label.config(text=f"Wrong! The correct answer is: {correct_answer}", fg="#ff0000")  # Red for incorrect answer
        
        self.disable_and_wait()

    # def disable_and_wait(self):
    #     self.button.config(state=tk.DISABLED)
    #     threading.Thread(target=self.wait_and_ask_question).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizkApp(root, "quizk_questions.csv")
    root.mainloop()
