# Mexc Python Demo

Before you use the demo, you need to generate your apikey & apisecret, then enter them first.

* <https://www.mexc.com/user/openapi>

## Spot V2、V3 Demo 

Fill in the corresponding function according to the parameters mentioned in the API documentation and execute it. => `print()`

**Rest API V2 doc**   `URL = 'https://www.mexc.com'`

* <https://mexcdevelop.github.io/apidocs/spot_v2_en/#introduction>

**Rest API V3 doc**   `URL = 'https://api.mexc.com'`

* <https://mexcdevelop.github.io/apidocs/spot_v3_en/#introduction>


> ### Example(Spot V3) :

Fill in your API key and Secret key in " python/spot/config.py "

```python
mexc_host = "https://api.mexc.com"
api_key = "your apikey"
secret_key = "your secretkey"
```

Select the corresponding file in the " python/run demo " folder to execute

Example " python/run demo/Market Data/ExchangeInfo.py "

```python
from python.spot import mexc_spot_v3

market = mexc_spot_v3.mexc_market()

# Enter parameters in JSON format in the "params", for example: {"symbol":"BTCUSDT", "limit":"200"}
# If there are no parameters, no need to send params
params = {
    "symbol": "BTCUSDT"
}
ExchangeInfo = market.get_exchangeInfo(params)
print(ExchangeInfo)
```

## Spot Websocket Demo 

According to the information you want to subscribe, change the content of the params according to the websocket documentation, ex: "op" or "symbol".   Execute the entire python file after adjusting the parameters.

**WebSocket doc**   `URL = 'wss://wbs.mexc.com/ws'`

* <https://mexcdevelop.github.io/apidocs/spot_v3_en/#websocket-market-streams>


> ### Example(Spot WebSocket) :
```python
import json
import websocket

BASE_URL = 'wss://wbs.mexc.com/ws'

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed ....")

def on_open(ws):
    params = {
        "method": "SUBSCRIPTION",
        "params":[
            "spot@public.deals.v3.api@BTCUSDT",
            "spot@public.kline.v3.api@BTCUSDT@Min5",
            "spot@public.increase.depth.v3.api@BTCUSDT",
            "spot@public.limit.depth.v3.api@BTCUSDT@5",
            "spot@public.bookTicker.v3.api@BTCUSDT"
        ]
    } 
    print(json.dumps(params))    
    ws.send(json.dumps(params))


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(BASE_URL,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                )
    ws.on_open = on_open
    ws.run_forever()

```
Для установки скопируйте папку python в виртуальное окружение и поменяйте файл .env
pip install python-dotenv
pip install requests
