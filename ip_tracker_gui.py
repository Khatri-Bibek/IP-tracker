import tkinter as tk

root = tk.Tk()
root.title("IP Tracker")
root.geometry("450x400")
root.resizable(False, False)

title_label = tk.Label(root, text="IP Address Tracker", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="Enter IP Address:").pack(pady=5)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

track_button = tk.Button(root, text="Track IP")
track_button.pack(pady=10)

root.mainloop()
