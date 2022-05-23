import pandas_datareader as pdr
import datetime as date
import yfinance as yf
import urllib3 as urllib3
import requests as requests

stocks = {}
def UpdateStocks(stockName, stockAmt):
    if stockName in stocks.keys():
        stocks[stockName] += stockAmt
    else:
        stocks[stockName] = 0

def GetStockValue(symbol):
    pg = yf.Ticker(symbol)
    data = pg.history(period='2d')
    price2 = data['Close'][1]
    return round(float(price2), 2)

def PrintStocks():
    for key in stocks:
        line = key + " x " + str(stocks[key])
        line += " = " + str(stocks[key] * GetStockValue(key))
        print(line)

# Ethical
symbol1 = "AAPL"
symbol2 = "ADBE"
symbol3 = "NSRGY"

# Growth
symbol1 = "BXP"
symbol2 = "DLR"
symbol3 = "EQT"

# Index
symbol1 = "VTI"
symbol2 = "IXUS"
symbol3 = "ILTB"

# Quality
symbol1 = "GOOGL"
symbol2 = "TSLA"
symbol3 = "NTDOY"

# Value
symbol1 = "BOOT"
symbol2 = "TPX"
symbol3 = "CRI"

def printInfo(symbol):
    print("\nOutput:")
    today = date.datetime.now().strftime('%a %b %d %H:%M:%S PDT %Y')
    print(today)

    pg = yf.Ticker(symbol)
    print(pg.info['longName'] + " (" + symbol + ")")
    data = pg.history(period='2d')
    price1 = data['Close'][0]
    price2 = data['Close'][1]
    diff = float(price2) - float(price1)
    percentChange = diff / float(price1) * 100

    sign = ""
    if diff >= 0:
        sign = "+"

    curPrice = "{:,.2f}".format(float(price2))
    priceChange = sign + "{:,.2f}".format(float(diff))
    percentDiff = sign + "{:,.2f}".format(float(percentChange))

    print(curPrice + " " + priceChange + " (" + percentDiff + "%)")
    return round(float(price2), 2)

priceA = printInfo(symbol1)
priceB = printInfo(symbol2)
priceC = printInfo(symbol3)

a = 0
b = 0
c = 0
investment = 5000
while investment > 0:
    if investment >= priceA:
        investment -= priceA
        a += 1
    else:
        break
    if investment >= priceB:
        investment -= priceB
        b += 1
    else:
        break
    if investment >= priceC:
        investment -= priceC
        c += 1
    else:
        break

print("\nStock Distribution:")
print(symbol1 + " = " + str(a))
print(symbol2 + " = " + str(b))
print(symbol3 + " = " + str(c))

print("\nPortfolio:")
UpdateStocks(symbol1, a)
UpdateStocks(symbol2, b)
UpdateStocks(symbol3, c)
PrintStocks()
