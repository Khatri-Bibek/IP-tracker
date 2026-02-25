import tkinter as tk

root = tk.Tk()
root.title("IP Tracker")
root.geometry("450x400")
root.resizable(False, False)

title_label = tk.Label(root, text="IP Address Tracker", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

root.mainloop()
