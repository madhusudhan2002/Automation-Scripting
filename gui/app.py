import tkinter as tk
from modules.system_monitor import SystemMonitor

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Automation Suite")
        self.monitor = SystemMonitor()

        tk.Label(self.root, text="System Monitor").pack()

        tk.Button(self.root, text="Check Status", command=self.show).pack()
        self.output = tk.Label(self.root, text="")
        self.output.pack()

    def show(self):
        status = self.monitor.get_status()
        self.output.config(text=str(status))

    def run(self):
        self.root.mainloop()
