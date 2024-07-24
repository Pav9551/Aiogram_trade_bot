from python.spot import mexc_spot_v3


trade = mexc_spot_v3.mexc_trade()

# Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
# If there are no parameters, no need to send params
params = {
    "symbol": "KASUSDT",
    "side": "BUY",
    "type": "LIMIT_MAKER",
    "price": "0.175",
    "quantity": "35"
}
PlaceOrder = trade.post_order(params)
print(PlaceOrder)


'''params = {
    "symbol": "KASUSDT",
    "side": "SELL",
    "type": "LIMIT",
    "price": "1.",
    "quantity": "8"
}'''
#{'symbol': 'KASUSDT', 'orderId': 'C02__443786925455765508018', 'orderListId': -1, 'price': '1', 'origQty': '8', 'type': 'LIMIT', 'side': 'SELL', 'transactTime': 1721589284057}
'''params = {
    "symbol": "KASUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "price": "0.185",
    "quantity": "35"
}'''
#{'symbol': 'KASUSDT', 'orderId': 'C02__443793362772922368018', 'orderListId': -1, 'price': '0.185', 'origQty': '35', 'type': 'LIMIT', 'side': 'BUY', 'transactTime': 1721590818833}

'''params = {
    "symbol": "KASUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "price": "0.177",
    "quantity": "35"
}'''
#{'symbol': 'KASUSDT', 'orderId': 'C02__444153484992913408018', 'orderListId': -1, 'price': '0.177', 'origQty': '35', 'type': 'LIMIT', 'side': 'BUY', 'transactTime': 1721676678661}
