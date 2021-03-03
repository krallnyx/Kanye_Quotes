from tkinter import *
import requests


class KanyeQuotes:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye Says...")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                                  font=("Arial", 20, "bold"), fill="white")
        self.canvas.grid(row=0, column=0)

        self.kanye_img = PhotoImage(file="kanye.png")
        self.kanye_button = Button(image=self.kanye_img, highlightthickness=0, command=self.get_quote)
        self.kanye_button.grid(row=1, column=0)

    def get_quote(self):
        response = requests.get(url="http://api.kanye.rest")
        response.raise_for_status()
        self.canvas.itemconfig(self.quote_text, text=response.json()["quote"])

        self.window.mainloop()


if __name__ == '__main__':
    kanye_quotes = KanyeQuotes()
    kanye_quotes.get_quote()

