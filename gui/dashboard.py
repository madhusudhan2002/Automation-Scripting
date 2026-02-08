import tkinter as tk
from tkinter import ttk
from modules.report_generator import ReportGenerator

class Dashboard:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Automation Suite Dashboard")
        self.root.geometry("800x500")

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        # Report Tab
        report_tab = ttk.Frame(notebook)
        notebook.add(report_tab, text="Report")

        self.text = tk.Text(report_tab)
        self.text.pack(fill="both", expand=True)

        tk.Button(report_tab, text="Refresh", command=self.refresh).pack()

        self.refresh()

    def refresh(self):
        report = ReportGenerator().generate_report()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, report)

    def run(self):
        self.root.mainloop()
