import tkinter as tk
from tkinter import messagebox

def convert_usd_to_pkr():
    try:
        usd_amount = float(usd_entry.get())
        usd_to_pkr_rate = float(usd_to_pkr_rate_entry.get())
        pkr_amount = usd_amount * usd_to_pkr_rate
        result_label.config(text=f"{usd_amount} USD = {pkr_amount:.2f} PKR")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for USD amount and exchange rate.")

def convert_btc_to_pkr():
    try:
        btc_amount = float(btc_entry.get())
        btc_to_usd_rate = float(btc_to_usd_rate_entry.get())
        usd_to_pkr_rate = float(usd_to_pkr_rate_entry.get())
        usd_value = btc_amount * btc_to_usd_rate
        pkr_amount = usd_value * usd_to_pkr_rate
        result_label.config(text=f"{btc_amount} BTC = {pkr_amount:.2f} PKR")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for BTC amount and exchange rates.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# USD to PKR Section
tk.Label(root, text="USD to PKR Conversion", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="USD to PKR Rate:").grid(row=1, column=0, sticky="e")
usd_to_pkr_rate_entry = tk.Entry(root)
usd_to_pkr_rate_entry.grid(row=1, column=1, padx=5)

tk.Label(root, text="Amount in USD:").grid(row=2, column=0, sticky="e")
usd_entry = tk.Entry(root)
usd_entry.grid(row=2, column=1, padx=5)

tk.Button(root, text="Convert USD to PKR", command=convert_usd_to_pkr).grid(row=3, column=0, columnspan=2, pady=10)

# BTC to PKR Section
tk.Label(root, text="BTC to PKR Conversion", font=("Arial", 14, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="BTC to USD Rate:").grid(row=5, column=0, sticky="e")
btc_to_usd_rate_entry = tk.Entry(root)
btc_to_usd_rate_entry.grid(row=5, column=1, padx=5)

tk.Label(root, text="Amount in BTC:").grid(row=6, column=0, sticky="e")
btc_entry = tk.Entry(root)
btc_entry.grid(row=6, column=1, padx=5)

tk.Button(root, text="Convert BTC to PKR", command=convert_btc_to_pkr).grid(row=7, column=0, columnspan=2, pady=10)

# Result Section
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
