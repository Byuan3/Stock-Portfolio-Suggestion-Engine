import datetime as date
import yfinance as yf


class StockEngine:
    def __init__(self):
        self.ethical = ['AAPL', 'ADBE', 'NSRGY']
        self.growth = ['BXP', 'DLR', 'EQT']
        self.index = ['VTI', 'IXUS', 'ILTB']
        self.quality = ['GOOGL', 'TSLA', 'NTDOY']
        self.value = ['BOOT', 'TPX', 'CRI']
        self.stocks = {}
        self.left = 0
        self.netValue = 0
        self.stockDf = {}
        self.data = [0, 0, 0, 0, 0]
        self.lastTimeChanged = date.datetime.now().day
        self.date = [(date.date.today() - date.timedelta(days=4)).strftime('%Y-%m-%d'),
                     (date.date.today() - date.timedelta(days=3)).strftime('%Y-%m-%d'),
                     (date.date.today() - date.timedelta(days=2)).strftime('%Y-%m-%d'),
                     (date.date.today() - date.timedelta(days=1)).strftime('%Y-%m-%d'),
                     date.date.today().strftime('%Y-%m-%d')]

    def reset(self):
        self.stocks = {}
        self.data = [0, 0, 0, 0, 0]
        self.netValue = 0

    def test(self):
        return self.netValue

    def updateData(self):
        self.data.append(self.netValue)
        self.data = self.data[1:6]
        self.date.append(date.date.today().strftime('%Y-%m-%d'))
        self.date = self.date[1:6]

    def updateTodayData(self):
        self.data[4] = self.netValue

    def updateDf(self):
        self.stockDf['AAPL'] = yf.Ticker('AAPL').history(period='1wk')
        self.stockDf['ADBE'] = yf.Ticker('ADBE').history(period='1wk')
        self.stockDf['NSRGY'] = yf.Ticker('NSRGY').history(period='1wk')

        self.stockDf['BXP'] = yf.Ticker('BXP').history(period='1wk')
        self.stockDf['DLR'] = yf.Ticker('DLR').history(period='1wk')
        self.stockDf['EQT'] = yf.Ticker('EQT').history(period='1wk')

        self.stockDf['VTI'] = yf.Ticker('VTI').history(period='1wk')
        self.stockDf['IXUS'] = yf.Ticker('IXUS').history(period='1wk')
        self.stockDf['ILTB'] = yf.Ticker('ILTB').history(period='1wk')

        self.stockDf['GOOGL'] = yf.Ticker('GOOGL').history(period='1wk')
        self.stockDf['TSLA'] = yf.Ticker('TSLA').history(period='1wk')
        self.stockDf['NTDOY'] = yf.Ticker('NTDOY').history(period='1wk')

        self.stockDf['BOOT'] = yf.Ticker('BOOT').history(period='1wk')
        self.stockDf['TPX'] = yf.Ticker('TPX').history(period='1wk')
        self.stockDf['CRI'] = yf.Ticker('CRI').history(period='1wk')

    def getStock(self, strategy):
        if strategy == 'e':
            return self.ethical
        if strategy == 'g':
            return self.growth
        if strategy == 'i':
            return self.index
        if strategy == 'q':
            return self.quality
        if strategy == 'v':
            return self.value

    def updateStocks(self, name, amt):
        if name in self.stocks.keys():
            self.stocks[name] += amt
        else:
            self.stocks[name] = amt

    def getStockValue(self, symbol):
        data = self.stockDf[symbol]
        price2 = data['Close'][1]
        return round(float(price2), 2)

    def printStock(self):
        line = ''
        for key in self.stocks:
            line = key + ' x ' + str(self.stocks[key])
            line += ' = ' + str(self.stocks[key] * self.getStockValue(key))
            line += '\n'
        return line

    def printInfo(self, symbol):
        line = "\nOutput:"
        line += '\n'
        line += date.datetime.now().strftime('%a %b %d %H:%M:%S PDT %Y')
        line += '\n'

        line += symbol + '\n'
        data = self.stockDf[symbol]
        price1 = data['Close'][-1]
        price2 = data['Close'][-2]
        diff = float(price2) - float(price1)
        percentChange = diff / float(price1) * 100

        sign = ""
        if diff >= 0:
            sign = "+"

        curPrice = "{:,.2f}".format(float(price2))
        priceChange = sign + "{:,.2f}".format(float(diff))
        percentDiff = sign + "{:,.2f}".format(float(percentChange))

        line += curPrice + " " + priceChange + " (" + percentDiff + "%)"
        line += '\n'

        return line, round(float(price2), 2)

    def addInvestment(self, strategy, amount):
        symbols = self.getStock(strategy)
        symbol1 = symbols[0]
        symbol2 = symbols[1]
        symbol3 = symbols[2]

        lineA, priceA = self.printInfo(symbol1)
        lineB, priceB = self.printInfo(symbol2)
        lineC, priceC = self.printInfo(symbol3)

        a = 0
        b = 0
        c = 0
        investment = amount
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

        self.updateStocks(symbol1, round(a * priceA, 2))
        self.updateStocks(symbol2, round(b * priceB, 2))
        self.updateStocks(symbol3, round(c * priceC, 2))
        self.netValue += round(a * priceA, 2)
        self.netValue += round(b * priceB, 2)
        self.netValue += round(c * priceC, 2)

        self.updateTodayData()

        return amount - investment

    def getStocks(self):
        return self.stocks
