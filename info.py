#@title Stock Shorthand
shorthandStock = "nke" #@param ["djia","mrk", "v", "mmm", "pg", "hd", "mcd", "wba", "ibm", "vz", "csco", "hon", "jnj", "unh", "trv", "ko", "amgn", "wmt", "crm", "axp", "gs", "dow", "cvx", "aapl", "stockInfo", "jpm", "intc", "cat", "nke", "dis", "ba"]
import yfinance as yf

stockInfo = yf.Ticker(shorthandStock)
# get stock info
dictionaryInfo = stockInfo.info
analyst = stockInfo.recommendations
stringsplits = ['open','previousClose','bid','ask','volume','pegRatio','forwardEps','trailingEps']
for x in stringsplits:
  print(x,":" , dictionaryInfo[x])
analyst