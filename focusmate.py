import tkinter as tk
import time

class FocusMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FocusMate - Study Tracker")
        self.time_left = 25 * 60
        self.running = False

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_btn = tk.Button(root, text="Start", command=self.start_timer)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.pause_btn = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

    def update_timer(self):
        if self.running:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.label.config(text=f"{minutes:02}:{seconds:02}")
            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.running = False
                self.label.config(text="Time's Up!")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.time_left = 25 * 60
        self.running = False
        self.label.config(text="25:00")

root = tk.Tk()
app = FocusMateApp(root)
root.mainloop()
