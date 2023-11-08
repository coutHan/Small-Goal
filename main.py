from traderClass import Trader

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Init
    trader = Trader()
    # Login
    trader.loginHelper.login()
    print("login complete!")
    # Show stats
    trader.showAllStocks()


