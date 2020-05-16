from nsetools import Nse
nse = Nse()

all_stock_codes = nse.get_stock_codes()

data = dict([(value, key) for key, value in all_stock_codes.items()])
st = 'Infosys'

def get_sym(st):
    for items in data.keys():
        if st.lower() in items.lower():
            sym = data[items]
    return sym

sym = get_sym(st)
print(sym)