import tkinter as tk
import random
from datetime import datetime
import matplotlib.pyplot as plt

# -------- Motivational Quotes --------
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is built on daily discipline.",
    "Small steps every day lead to big changes.",
    "Don't stop when you're tired. Stop when you're done.",
    "You are stronger than you think.",
    "Discipline is doing it even when you don't feel like it.",
    "Study now, shine later.",
    "Your only limit is your mind.",
    "Every day is a chance to get better.",
    "Stay focused. Stay determined. Stay strong."
]

# -------- Global Variables --------
time_left = 0
timer_running = False
countdown_id = None
quote_id = None
daily_progress = {}
current_session_minutes = 0

# -------- Main Window --------
root = tk.Tk()
root.title("🎯 FocusMate - Study Timer & Motivation")
root.geometry("620x520")
root.configure(bg="#f9f9f9")
# root.iconbitmap("focusmate.ico")  # Optional: Add your icon here

# -------- Title --------
title = tk.Label(root, text="📚 FocusMate", font=("Verdana", 26, "bold"), bg="#f9f9f9", fg="#2c3e50")
title.pack(pady=10)

# -------- Entry Section --------
entry_frame = tk.Frame(root, bg="#f9f9f9")
entry_frame.pack()

entry_label = tk.Label(entry_frame, text="Set Timer (minutes): ", font=("Arial", 12), bg="#f9f9f9")
entry_label.grid(row=0, column=0, padx=5)

time_entry = tk.Entry(entry_frame, font=("Arial", 14), width=5, justify="center", bg="#e8f0fe")
time_entry.grid(row=0, column=1, padx=5)

# -------- Timer Display --------
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 42, "bold"), bg="#f9f9f9", fg="#222")
timer_label.pack(pady=15)

# -------- Quote Display --------
quote_label = tk.Label(root, text="", font=("Georgia", 13, "italic"), wraplength=500,
                       justify="center", bg="#f9f9f9", fg="#2d572c")
quote_label.pack(pady=15)

# -------- Timer Functions --------
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def update_timer():
    global time_left, countdown_id, timer_running
    if timer_running and time_left > 0:
        timer_label.config(text=format_time(time_left))
        time_left -= 1
        countdown_id = root.after(1000, update_timer)
    elif time_left == 0 and timer_running:
        timer_label.config(text="00:00")
        quote_label.config(text="⏳ Time's up! Great job!")
        add_to_progress(current_session_minutes)
        stop_timer()

def update_quote():
    global quote_id
    if timer_running:
        quote = random.choice(quotes)
        quote_label.config(text=quote)
        quote_id = root.after(10000, update_quote)

def start_timer():
    global time_left, timer_running, current_session_minutes
    if not timer_running:
        try:
            mins = int(time_entry.get())
            time_left = mins * 60
            current_session_minutes = mins
            if time_left <= 0:
                quote_label.config(text="⚠️ Enter time greater than 0.")
                return
            timer_running = True
            update_timer()
            update_quote()
        except ValueError:
            quote_label.config(text="⚠️ Please enter a valid number.")

def stop_timer():
    global timer_running
    timer_running = False
    if countdown_id:
        root.after_cancel(countdown_id)
    if quote_id:
        root.after_cancel(quote_id)
    timer_label.config(text="Stopped")
    quote_label.config(text="⏸ Timer Stopped")

def reset_timer():
    global timer_running, time_left, current_session_minutes
    stop_timer()
    time_left = 0
    current_session_minutes = 0
    timer_label.config(text="00:00")
    quote_label.config(text="")
    time_entry.delete(0, tk.END)

# -------- Progress Tracker --------
def add_to_progress(minutes):
    today = datetime.now().strftime("%Y-%m-%d")
    if today in daily_progress:
        daily_progress[today] += minutes
    else:
        daily_progress[today] = minutes

def show_progress_chart():
    if not daily_progress:
        quote_label.config(text="📊 No progress data available yet.")
        return
    dates = list(daily_progress.keys())
    minutes = list(daily_progress.values())
    plt.figure(figsize=(8, 4))
    plt.bar(dates, minutes, color="#4CAF50")
    plt.xlabel("Date")
    plt.ylabel("Minutes Studied")
    plt.title("📈 Daily Study Progress")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -------- Buttons --------
btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=15)

start_btn = tk.Button(btn_frame, text="▶ Start", command=start_timer, width=10, bg="#d4edda", font=("Arial", 11))
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(btn_frame, text="⏹ Stop", command=stop_timer, width=10, bg="#f8d7da", font=("Arial", 11))
stop_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(btn_frame, text="🔁 Reset", command=reset_timer, width=10, bg="#ffeeba", font=("Arial", 11))
reset_btn.grid(row=0, column=2, padx=10)

chart_btn = tk.Button(root, text="📊 Show Progress Chart", command=show_progress_chart,
                      width=25, bg="#cce5ff", font=("Arial", 11))
chart_btn.pack(pady=10)

# -------- Run GUI --------
root.mainloop()
