from python.spot import mexc_spot_v3


listenkey = mexc_spot_v3.mexc_listenkey()

# Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
# If there are no parameters, no need to send params
params = {
    "listenKey": "c3ea30ceaf7dfdc4a3541e46747214b6871cba517b32f5778c0855e3903dbbc7"
}
DeleteListenKey = listenkey.delete_listenKey(params)
print(DeleteListenKey)
