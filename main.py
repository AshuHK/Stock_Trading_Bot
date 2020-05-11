import time
import alpaca_trade_api as trade_api 
from alpaca_trade_api import StreamConn



class TradingBot: 
    def __init__(self, api, connection): 
        self.api = api
        self.connection = connection
    
    def run(self): 
        async def on_minute(connection, channel, bar): 

            # using the Doji Candle method to choose when tp buy 
            if (bar.close >= bar.open) and ((bar.open - bar.low) >= 0.1): 
                print("Buying on Doji Candle")
                self.api.submit_order("TSLA", 1, "buy", "market", "day")
            
            # take profit at one percent 

        # set up the running of the bot 
        on_minute = self.connection.on(r"AM$")(on_minute)

        connection.run(["AM.TSLA"])


def parse_keys(file_obj): 
    keys_dict = {} 

    for line in file_obj: 
        line_list = line.split(":")
        keys_dict[line_list[0]] = line_list[1].strip("\n").strip(" ").strip("\t")

    return keys_dict


def main(): 

    # use the template for to create api_keys.txt
    file_obj = open("api_keys.txt", "r")
    keys_dict = parse_keys(file_obj)

    # setting this up for a paper trading account 
    trade_url = "https://paper-api.alpaca.markets"
    data_url = "https://data.alpaca.markets/v1"


    # Use the REST API using the keys from Alpaca and the paper trading site 
    api = trade_api.REST(keys_dict["key"], keys_dict["secret"], trade_url, api_version="v2")

    connection = StreamConn(keys_dict["key"], keys_dict["secret"], data_url)

    trade_bot = TradingBot(api, connection)

    return None 

if __name__ == "__main__": 
    main() 
