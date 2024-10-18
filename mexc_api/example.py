from mexc_api.mexcClass import mexc_trade
query_parameters = {
            'price': 0.1,
            'quantity': 10,
            'side': 'BUY',
            'symbol': 'KASUSDT',
            'type': 'LIMIT'
        }
mexc = mexc_trade()
#mexc.post_order(query_parameters)
print(mexc.create_listen_key())
