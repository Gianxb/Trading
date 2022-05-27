import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"Part 1: Import of the Historical Stock Data of the Dow Jones from 2000 to 2022 on a quarterly basis."
url = 'https://raw.githubusercontent.com/Gianxb/Trading/main/Trading.csv'
df = pd.read_csv(url, sep=",")
dg = pd.DataFrame(df.loc [:, ' Close'].values, df.loc [:, 'Date'].values)

"Part 2: Defining the most important events, that influenced the chart imported in Part 1 (The number represents the quarter of a year e.g. 6 --> 2nd Quarter of 2001)."
events = {
    6: "Burst of the Dot-Com Bubble",
    78: "Lehman collapse",
    82: "Financial Crises comes to an end",
    138: "Chinese Stock Market Crash",
    148: "Brexit Referendum Agreement",
    151: "Election of Donald Trump",
    168: "United States of America Trade Ban",
    180: "Global Pandemic Recession"
    }

"Part 3: Define a variable for the number of Quarters. The number of Quarters are the same as in the dictionary (The number represents the quarter of a year e.g. 6 --> 2nd Quarter of 2001)."
i=1

"Part 4: Defining a Class for the Trader. Every Trader starts with 100000 CHF and 0 stocks." 
class Tradingaccount:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.amount = 100000
        self.stocks = 0
    def buy(self, x):
        self.amount -= x * dg.iloc[i].values
        self.stocks += x
    def sell(self, x):
        self.amount += x * dg.iloc[i].values
        self.stocks -= x

"Part 5: For the Class every Trader defines a name and a age. Only adults are allowed to trade!" 
name = input ("This is a trading game, based on quarterly Dow Jones events. For certain events you can either buy or sell the underlying stocks. Please insert your name. ")

try:
    age = int(input(f"Welcome to the trading world {name}. Please insert your age."))
    
    "Part 6: Only allow adults to trade."
    if age >= 18:
        t1 = Tradingaccount(name, age)
        print(f"Alright {t1.name}. You start with {t1.amount} CHF, to trade. Starting the Trading right now!")
        
        "Part 7: Draw the Trading Chart with the data from Part 1."
        for i in range(200):
            i+=1
            dh = dg.head(i)
            plt.figure(figsize=(1000,1000))
            dh.plot()
            plt.draw()
            plt.pause(0.0001)
            
            "Part 8: With an Event from Part 2, a trader can decide between holding, buying or selling stock." 
            if i in events:
                j = 1
                while j < 2:
                    answer = input(f"Event on the {df.iloc[i,0]}: {events[i]}! Would you like to hold, buy or sell stock at the current price of {dg.iloc[i].values} CHF? (type: 'hold', 'buy' or 'sell')")
                    if answer == "hold":
                        j += 1
                    elif answer == "buy":
                        k = 1
                        while k < 2:
                            buyamount = int(input("How many stocks would you like to buy?"))
                            if buyamount * dg.iloc[i].values > t1.amount:
                                print(f"You can buy a maximum of {t1.amount / dg.iloc[i].values} stocks")
                                continue
                            elif buyamount < 0:
                                print(f"Has to be a positive amount")
                                continue
                            else:
                                t1.buy(buyamount)
                                k += 1
                        j += 1
                    elif answer == "sell":
                        k = 1
                        while k < 2:
                            sellamount = int(input("How many stocks would you like to sell?"))
                            if sellamount > t1.stocks:
                                print(f"You can sell a maximum of {t1.stocks} stocks")
                            elif sellamount < 0:
                                print(f"Has to be a positive amount")
                                continue
                            else:
                                t1.sell(sellamount)
                                k += 1
                        j += 1
                        
        "Part 9: At the last date, the remaining stock are automatically sold at the current price." 
        if t1.stocks > 0:
            t1.sell(t1.stocks)
            
        "Part 10: The return of the trades are shown to the trader." 
        if t1.amount > 100000:
            print(f"Congratulations {t1.name}, your return on the Dow Jones is {t1.amount-100000} CHF")
        else:
            print(f"Oh no! {t1.name}, your return on the Dow Jones is {t1.amount-100000} CHF")
    else:
        print("By law underage people are to be protected. You are not allowed to trade!")
except ValueError:
    print ("Age should be a number)