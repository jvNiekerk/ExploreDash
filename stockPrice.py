import yfinance as yf
import argparse

#Add parser
parser = argparse.ArgumentParser(description='You can add a description here')
parser.add_argument('-n','--name', help='Your name',required=True)
args = parser.parse_args()

#define the ticker symbol
tickerSymbol = args.name

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#see your data
print(tickerDf)