from loginClass import Login
import robin_stocks.robinhood as r


class Trader:
    # This is the main class for this trading bot
    loginHelper = Login()

    def __init__(self):
        print("Trader init...")

    def showAllStocks(self):
        print(self.getAllStocks())

    def getAllStocks(self):
        my_stocks = r.build_holdings()
        return my_stocks.items()

