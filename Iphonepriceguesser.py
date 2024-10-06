import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression

class PriceGuesser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Price Guesser")

        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Helvetica', 12))

        self.entry_label = ttk.Label(self.root, text="Enter iPhone Version:")
        self.entry_label.pack(pady=10)

        self.entry1 = ttk.Entry(self.root)
        self.entry1.pack(pady=10)

        self.button1 = ttk.Button(self.root, text="Predict Price", command=self.predict_price)
        self.button1.pack(pady=10)

        self.data = pd.read_csv("priceguesserofiphone.csv")

        self.model = LinearRegression()
        self.model.fit(self.data[["version"]], self.data["price"])

        self.label_result = ttk.Label(self.root, text="")
        self.label_result.pack(pady=10)

        self.root.mainloop()

    def predict_price(self):
        try:
            model_to_predict = float(self.entry1.get())
            predicted_price = self.model.predict([[model_to_predict]])
            predicted_price = predicted_price[0]

            result_text = f"Predicted price for iPhone {model_to_predict}: {predicted_price:.2f}"
        except ValueError:
            result_text = "Please enter a valid numeric value."

        self.label_result.config(text=result_text)

app = PriceGuesser()
