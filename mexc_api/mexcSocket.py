import json
import traceback
import websocket
import threading
#https://www.mexc.com/ru-RU/support/articles/17827791508659
class Socket_conn_MEXC(websocket.WebSocketApp):
    def __init__(self, url):
        super().__init__(
            url=url,
            on_open=self.on_open,
            on_close=self.on_close,
            on_message=self.on_message,
            on_error=self.on_error
        )
        self.run_forever()
    def on_message(self,ws,msg):
        data = json.loads(msg)
        print(data)
    def on_open(self, ws):
        print(ws,'Websocket was opend')
        subscription_message = {
            "method": "SUBSCRIPTION",
            "params": params
        }
        ws.send(json.dumps(subscription_message))
    def on_error(self,ws,error):
        print('on_error',ws,error)
        print(traceback.format_exc())
        exit()
    def on_close(self,ws,status,msg):
        data = json.loads(msg)
        print(data)
params = ["spot@public.increase.depth.v3.api@KASUSDT"]
url =  "wss://wbs.mexc.com/ws"
threading.Thread(target=Socket_conn_MEXC,args=(url,)).start()

