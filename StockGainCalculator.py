from tkinter import *
from tkinter.ttk import Notebook
from customtkinter import *
from Calculations import profitOrLossFunction, stockAverageFunction

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.title("Stock Calculator")
root['bg'] = 'white'

tabControl = Notebook(root)

tab1 = Frame(tabControl)
tabControl.add(tab1, text="Stock Profit Calculator")
tabControl.pack(expand=1, fill="both")

tab2 = Frame(tabControl)
tabControl.add(tab2, text="Average Down Calculator")
tabControl.pack(expand=1, fill="both")


# ----------------------------- TAB 1 -------------------------

def activateProfit():
    result = profitOrLossFunction(numSharesEntry.get(), purchasePriceEntry.get(), sellPriceEntry.get())
    emptylabel.config(text=result)


def tab1Reset():
    emptylabel.config(text="")
    numSharesEntry.delete(0, END)
    purchasePriceEntry.delete(0, END)
    sellPriceEntry.delete(0, END)


generalCanvas = Canvas(tab1, bg='gray', width=500, height=500)
generalCanvas.place(x=-1, y=-1)

profitLossTitle = CTkLabel(tab1, text="Profit/Loss Calculator", height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                           text_font=1, bg_color="gray")
profitLossTitle.place(x=150, y=20)

numShares = CTkLabel(master=tab1, text='Number of Shares', height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                     text_font=1, bg_color="gray")
numShares.grid(row=0, column=0, padx=(5, 0), pady=(65, 0))

numSharesEntry = CTkEntry(master=tab1, width=220, bg_color="gray")
numSharesEntry.grid(row=0, column=1, padx=(5, 0), pady=(71, 10))

purchasePrice = CTkLabel(master=tab1, text="Purchase Price ($)", height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                         text_font=1, bg_color="gray")
purchasePrice.grid(row=1, column=0, padx=(5, 0), pady=10)

purchasePriceEntry = CTkEntry(master=tab1, width=220, bg_color="gray")
purchasePriceEntry.grid(row=1, column=1, padx=(5, 0), pady=10)

sellPrice = CTkLabel(master=tab1, text="Sell Price ($)", height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                     text_font=1, bg_color="gray")
sellPrice.grid(row=2, column=0, padx=(5, 0), pady=10)

sellPriceEntry = CTkEntry(master=tab1, width=220, bg_color="gray")
sellPriceEntry.grid(row=2, column=1, padx=(5, 0))

sellPrice = CTkLabel(master=tab1, text="result", height=40, fg_color=("gray", "black"), justify=tkinter.LEFT, text_font=1,
                     bg_color="gray")
sellPrice.grid(row=3, column=0, padx=(5, 0), pady=10)

emptylabel = Label(tab1, fg='green', font=('arial', 14))
emptylabel.grid(row=3, column=1, sticky=W, pady=10)

activateProfitButton = CTkButton(master=tab1, command=activateProfit, text='Calculate', bg_color="gray")
activateProfitButton.grid(row=4, column=1, sticky=W)

resetButton = Button(master=tab1, command=tab1Reset, text='Reset')
resetButton.place(x=450, y=10)


# ------------------------------END TAB 1-------------------------------

# ----------------------------- TAB 2 -------------------------

def activateAverage():
    result2 = stockAverageFunction([share_bought_1.get(), share_bought_2.get(), share_bought_3.get(), share_bought_4.get(), purchase_price_1.get(), purchase_price_2.get(), purchase_price_3.get(), purchase_price_4.get()])
    emptylabel1.config(text=result2)

def tab2Reset():
    emptylabel1.config(text="")
    share_bought_1.delete(0, END)
    purchase_price_1.delete(0, END)
    share_bought_2.delete(0, END)
    purchase_price_2.delete(0, END)
    share_bought_3.delete(0, END)
    purchase_price_3.delete(0, END)
    share_bought_4.delete(0, END)
    purchase_price_4.delete(0, END)



generalCanvas = Canvas(tab2, bg='gray', width=500, height=500)
generalCanvas.place(x=-1, y=-1)

profitLossTitle = CTkLabel(tab2, text="Stock Average Calculator", height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                           text_font=1, bg_color="gray")
profitLossTitle.place(x=150, y=20)

numShares = CTkLabel(tab2, text='Shares Bought', height=40, fg_color=("white", "black"), justify=tkinter.LEFT, text_font=1,
                     bg_color="gray")
numShares.grid(row=0, column=0, padx=(5, 0), pady=(75, 0))

purchasePrice = CTkLabel(tab2, text='Purchase Price', height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                         text_font=1, bg_color="gray")
purchasePrice.grid(row=0, column=1, padx=(5, 0), pady=(75, 0))

share_bought_1 = CTkEntry(master=tab2, width=220, bg_color="gray")
share_bought_1.grid(row=1, column=0, padx=(25, 0), pady=(10, 0))

purchase_price_1 = CTkEntry(master=tab2, width=220, bg_color="gray")
purchase_price_1.grid(row=1, column=1, padx=(25, 0), pady=(10, 0))

share_bought_2 = CTkEntry(master=tab2, width=220, bg_color="gray")
share_bought_2.grid(row=2, column=0, padx=(25, 0), pady=10)

purchase_price_2 = CTkEntry(master=tab2, width=220, bg_color="gray")
purchase_price_2.grid(row=2, column=1, padx=(25, 0), pady=10)

share_bought_3 = CTkEntry(master=tab2, width=220, bg_color="gray")
share_bought_3.grid(row=3, column=0, padx=(25, 0), pady=10)

purchase_price_3 = CTkEntry(master=tab2, width=220, bg_color="gray")
purchase_price_3.grid(row=3, column=1, padx=(25, 0))

share_bought_4 = CTkEntry(master=tab2, width=220, bg_color="gray")
share_bought_4.grid(row=4, column=0, padx=(25, 0), pady=10)

purchase_price_4 = CTkEntry(master=tab2, width=220, bg_color="gray")
purchase_price_4.grid(row=4, column=1, padx=(25, 0))

resultLabel = CTkLabel(master=tab2, text="result", height=40, fg_color=("white", "black"), justify=tkinter.LEFT,
                       text_font=1, bg_color="gray")
resultLabel.grid(row=5, column=0, padx=(5, 0), pady=10)

emptylabel1 = Label(tab2, fg='green', font=('arial', 14))
emptylabel1.grid(row=5, column=1, sticky=W, pady=10)

button3 = CTkButton(master=tab2, command=activateAverage, text='Calculate', bg_color="gray")
button3.grid(row=6, column=1, sticky=W)

one = CTkLabel(tab2, text="1.", height=1, width=0, fg_color=("red", "gray"), justify=tkinter.LEFT, text_font=1,
               bg_color="gray")
one.place(x=1, y=130)

two = CTkLabel(tab2, text="2.", height=1, width=0, fg_color=("red", "gray"), justify=tkinter.LEFT, text_font=1,
               bg_color="gray")
two.place(x=1, y=170)

three = CTkLabel(tab2, text="3.", height=1, width=0, fg_color=("red", "gray"), justify=tkinter.LEFT, text_font=1,
                 bg_color="gray")
three.place(x=1, y=220)

four = CTkLabel(tab2, text="4.", height=1, width=0, fg_color=("red", "gray"), justify=tkinter.LEFT, text_font=1,
                bg_color="gray")
four.place(x=1, y=270)

resetButton1 = Button(master=tab2, command=tab2Reset, text='Reset')
resetButton1.place(x=450, y=10)

# ------------------------------END TAB 2-------------------------------


root.mainloop()

