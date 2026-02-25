import tkinter as tk
from tkinter import messagebox
import requests

def track_ip():
    ip = entry.get()

    # ✅ Input validation
    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address")
        return

    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    result_text.delete("1.0", tk.END)

    for key, value in data.items():
        result_text.insert(tk.END, f"{key}: {value}\n")

root = tk.Tk()
root.title("IP Tracker")
root.geometry("450x400")
root.resizable(False, False)

title_label = tk.Label(root, text="IP Address Tracker", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="Enter IP Address:").pack(pady=5)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

track_button = tk.Button(root, text="Track IP", command=track_ip)
track_button.pack(pady=10)

tk.Label(root, text="Results:").pack(pady=5)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
