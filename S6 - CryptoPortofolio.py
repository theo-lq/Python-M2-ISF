import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import cryptocompare







class Portofolio:
    
    def __init__(self, initial_investment, coins):
        self.initial_investment = initial_investment
        self.coins = coins
        self.portofolio_stacks, self.portofolio_amount = self.initialize_portofolio()
    
    
    
    def initialize_portofolio(self):
        portofolio_stacks, portofolio_amount = {}, {}
        
        for coin in self.coins:
            price = cryptocompare.get_price(coin, currency="EUR")[coin]["EUR"]
            portofolio_stacks[coin] = self.initial_investment / (len(coins) * price)
            portofolio_amount[coin] = portofolio_stacks[coin] * price
        
        return portofolio_stacks, portofolio_amount
    
    
    
    def update_value(self):
        for coin in self.coins:
            price = cryptocompare.get_price(coin, currency="EUR")[coin]["EUR"]
            self.portofolio_amount[coin] = self.portofolio_stacks[coin] * price
    
    
    
    def print_value(self):
        total = 0
        
        for coin in self.coins:
            total += self.portofolio_amount[coin]
            print("%s: %0.2f€" % (coin, self.portofolio_amount[coin]))
        
        returns = 100 * (round(total, 2) / self.initial_investment - 1)
        print("Total: %0.2f€, return=%0.4f" % (total, returns) + "%")
    





initial_investment = 1000
coins = ["ETH", "BNB", "UNI", "TRX", "XLM", "LTC"]



portofolio = Portofolio(initial_investment, coins)


from time import time, sleep
from os import system
for i in range(5):
    portofolio.update_value()
    system('clear')
    portofolio.print_value()
    sleep(60)
    

