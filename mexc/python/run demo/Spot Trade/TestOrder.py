from python.spot import mexc_spot_v3


trade = mexc_spot_v3.mexc_trade()

# Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
# If there are no parameters, no need to send params
params = {
    "symbol": "KASUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "price": "0.176",
    "quantity": "7"
}
TestOrder = trade.post_order_test(params)
print(TestOrder)
