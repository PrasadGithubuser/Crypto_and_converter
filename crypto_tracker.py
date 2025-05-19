import tkinter as tk
from tkinter import ttk
import requests

crypto_names = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "dogecoin": "Dogecoin",
    "solana": "Solana",
    "litecoin": "Litecoin",
    "cardano": "Cardano"
}
 
currencies = ["usd", "inr", "eur", "gbp"]

def get_crypto_price():
    coin = crypto_var.get()
    currency = currency_var.get()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[coin][currency]
        price_label.config(text=f"{crypto_names[coin]} Price: {price} {currency.upper()}")
    except:
        price_label.config(text="Error fetching price.")


def convert_currency():
    from_curr = from_var.get()
    to_curr = to_var.get()
    amount = amount_entry.get()

    if not amount.isdigit():
        result_label.config(text="Enter a valid amount.")
        return

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
    try:
        response = requests.get(url)
        data = response.json()
        converted = data["rates"][to_curr]
        result_label.config(text=f"{amount} {from_curr} = {converted:.2f} {to_curr}")
    except:
        result_label.config(text="Error converting currency.")


root = tk.Tk()
root.title("💰 Crypto Tracker & Currency Converter")
root.geometry("500x400")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Tab-1

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Crypto Price Tracker")

tk.Label(tab1, text="Select Crypto:", font=("Arial", 12)).pack(pady=5)
crypto_var = tk.StringVar(value="bitcoin")
ttk.Combobox(tab1, textvariable=crypto_var, values=list(crypto_names.keys()), state="readonly").pack()

tk.Label(tab1, text="Select Currency:", font=("Arial", 12)).pack(pady=5)
currency_var = tk.StringVar(value="usd")
ttk.Combobox(tab1, textvariable=currency_var, values=currencies, state="readonly").pack()

tk.Button(tab1, text="Get Price", command=get_crypto_price, bg="#0066cc", fg="white").pack(pady=10)

price_label = tk.Label(tab1, text="", font=("Arial", 14), fg="green")
price_label.pack(pady=20)

# Tab-2

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Currency Converter")

tk.Label(tab2, text="From:", font=("Arial", 12)).pack(pady=5)
from_var = tk.StringVar(value="USD")
ttk.Combobox(tab2, textvariable=from_var, values=["USD", "INR", "EUR", "GBP"], state="readonly").pack()

tk.Label(tab2, text="To:", font=("Arial", 12)).pack(pady=5)
to_var = tk.StringVar(value="INR")
ttk.Combobox(tab2, textvariable=to_var, values=["USD", "INR", "EUR", "GBP"], state="readonly").pack()

tk.Label(tab2, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(tab2)
amount_entry.pack()

tk.Button(tab2, text="Convert", command=convert_currency, bg="#28a745", fg="white").pack(pady=10)

result_label = tk.Label(tab2, text="", font=("Arial", 14), fg="purple")
result_label.pack(pady=20)

root.mainloop()
