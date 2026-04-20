import tkinter as tk

# Quiz Data
quiz = [
    {"question": "What is the capital of India?",
     "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
     "answer": "Delhi"},
    {"question": "Which language is used for web development?",
     "options": ["Python", "C++", "HTML", "Java"],
     "answer": "HTML"},
    {"question": "What is 5 + 3?",
     "options": ["6", "7", "8", "9"],
     "answer": "8"},
    {"question": "Who is the father of computers?",
     "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Elon Musk"],
     "answer": "Charles Babbage"},
    {"question": "What is the color of the sky?",
     "options": ["Blue", "Green", "Red", "Yellow"],
     "answer": "Blue"}
]

# Variables
q_index = 0
score = 0
username = ""

# Window
root = tk.Tk()
root.title("Basic Quiz Game 🎯")
root.geometry("500x400")
root.config(bg="white")

# ----------- FRONT PAGE -----------
front_frame = tk.Frame(root, bg="white")
front_frame.pack(fill="both", expand=True)

tk.Label(front_frame, text="Basic Quiz Game",
         font=("Arial", 22, "bold"),
         fg="#008060", bg="white").pack(pady=80)

def go_to_name():
    front_frame.pack_forget()
    name_frame.pack(fill="both", expand=True)

tk.Button(front_frame, text="Start",
          font=("Arial", 14, "bold"),
          bg="#00cc66", fg="white",
          width=15,
          command=go_to_name).pack()

# ----------- NAME PAGE -----------
name_frame = tk.Frame(root, bg="white")

tk.Label(name_frame, text="Enter your name:",
         font=("Arial", 14),
         bg="white").pack(pady=40)

name_entry = tk.Entry(name_frame, font=("Arial", 12))
name_entry.pack()

def start_quiz():
    global username
    username = name_entry.get()
    
    if username == "":
        return
    
    name_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    load_question()

tk.Button(name_frame, text="Continue",
          font=("Arial", 12, "bold"),
          bg="#00cc66", fg="white",
          command=start_quiz).pack(pady=20)

# ----------- QUIZ PAGE -----------
quiz_frame = tk.Frame(root, bg="white")

question_label = tk.Label(quiz_frame, text="",
                          font=("Arial", 14, "bold"),
                          bg="white", wraplength=400)
question_label.pack(pady=20)

def select_option(value):
    global q_index, score
    
    if value == quiz[q_index]["answer"]:
        score += 1
    
    q_index += 1
    
    if q_index < len(quiz):
        load_question()
    else:
        show_result_page()

buttons = []
for i in range(4):
    btn = tk.Button(quiz_frame, text="",
                    font=("Arial", 12),
                    bg="#00cc66", fg="white",
                    width=30)
    btn.pack(pady=8)
    buttons.append(btn)

def load_question():
    q = quiz[q_index]
    question_label.config(text=f"{q_index+1}. {q['question']}")
    
    for i in range(4):
        buttons[i].config(
            text=q["options"][i],
            command=lambda val=q["options"][i]: select_option(val)
        )

# ----------- RESULT PAGE -----------
result_frame = tk.Frame(root, bg="white")

def show_result_page():
    quiz_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)

    total = len(quiz)
    percentage = (score / total) * 100

    if percentage == 100:
        performance = "Excellent 🌟"
    elif percentage >= 60:
        performance = "Good 👍"
    else:
        performance = "Needs Improvement 💪"

    tk.Label(result_frame, text="Quiz Result",
             font=("Arial", 20, "bold"),
             fg="#008060", bg="white").pack(pady=20)

    tk.Label(result_frame, text=f"Name: {username}",
             font=("Arial", 14), bg="white").pack(pady=5)

    tk.Label(result_frame, text=f"Marks: {score}/{total}",
             font=("Arial", 14), bg="white").pack(pady=5)

    tk.Label(result_frame, text=f"Percentage: {percentage:.2f}%",
             font=("Arial", 14), bg="white").pack(pady=5)

    tk.Label(result_frame, text=f"Performance: {performance}",
             font=("Arial", 14), bg="white").pack(pady=10)

    tk.Button(result_frame, text="Exit",
              font=("Arial", 12, "bold"),
              bg="#00cc66", fg="white",
              command=root.destroy).pack(pady=20)

# Run app
root.mainloop()
