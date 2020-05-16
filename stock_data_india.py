from nsetools import Nse
import pandas as pd
nse = Nse()

all_stock_codes = nse.get_stock_codes()
data = dict([(value, key) for key, value in all_stock_codes.items()])

# top_gain = nse.get_top_gainers()
# top_loser = nse.get_top_losers()


def get_sym(st):
    for items in data.keys():
        if st.lower() in items.lower():
            sym = data[items]
    return sym

def get_price_ind(stock):
    sym = get_sym(stock)
    price = nse.get_quote(sym)['buyPrice1']
    high = nse.get_quote(sym)['dayHigh']
    low = nse.get_quote(sym)['dayLow']
    open = nse.get_quote(sym)['open']
    q = {'Price: ': price, 'High: ': high, 'Low: ': low, 'Open: ': open}
    return pd.DataFrame(q.items(), columns=['', ''])

def get_topgain():
    top_gain = nse.get_top_gainers()
    sym = top_gain['symbol']
    openp = top_gain['openPrice']
    highp = top_gain['highPrice']
    lowp = top_gain['lowPrice']
    q1 = {'Name: ':sym, 'Open: ':openp, 'High: ':highp, 'Low: ':lowp}
    return pd.DataFrame(q1.items(), columns=['', ''])

def get_toploss():
    top_gain = nse.get_top_losers()
    sym = top_gain['symbol']
    openp = top_gain['openPrice']
    highp = top_gain['highPrice']
    lowp = top_gain['lowPrice']
    q2 = {'Name: ':sym, 'Open: ':openp, 'High: ':highp, 'Low: ':lowp}
    return pd.DataFrame(q2.items(), columns=['', ''])
