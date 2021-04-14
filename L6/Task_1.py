coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

def tpl_to_dict():
    dict = {coin[i]: code[i] for i in range(len(coin))}
    print(dict)
