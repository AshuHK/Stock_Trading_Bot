import time
import alpaca_trade_api as trade_api
from alpaca_trade_api import StreamConn


class TradingBot:
    def __init__(self, api, connection):
        self.api = api
        self.connection = connection

    def run(self):
        async def on_minute(connection, channel, bar):
            """
            For each minute that has passed in the data stream continuously, 
            do a trade (buy or sell dependant on the position) 

            :param connection: StreamConn that represents the data stream 
            :param channel: Channel for the specific stock you want to trade 
            :param bar: Bar for the specific stock being watched 
            """
            symbol = bar.symbol

            # basic debug output (change if needed)
            print("Close: {}".format(bar.close))
            print("Open: {}".format(bar.open))
            print("Low: {}".format(bar.low))
            print(symbol)

            # buy when the Doji candle forms
            if (bar.close > bar.open) and (bar.open - bar.low > 0.1):
                print("Buying on Doji")
                self.api.submit_order(symbol, 1, "buy", "market", "day")

            # taking profit at 1 percent (Not sure if this is right)
            if (bar.open > bar.close) and (bar.open - bar.low < (bar.open * 0.01)):
                print("Selling at 1% profit")
                self.api.submit_order(symbol, 1, "sell", "market", "day")

        # set up the running of the bot
        on_minute = self.connection.on(r"AM$")(on_minute)

        # Change TSLA for any stock that you want to trade here
        self.connection.run(["AM.TSLA"])


def parse_keys(file_obj):
    """
    Parses the given file to get the keys for the Alpaca/Polygon API keys

    :param file_obj: File pointer to iterate through the file 

    :return: a dictionary of the {key type : key} parings as strings  
    """
    keys_dict = {}

    # iterate through the whole file and split at the color
    for line in file_obj:
        line_list = line.split(":")

        # also trims all white spcae on both ends just in case
        keys_dict[line_list[0]] = line_list[1].strip("\n").strip(" ").strip("\t")

    return keys_dict


def main():

    # use the templates for to create alpaca_api_keys.txt and polygon_api_keys.txt
    alpaca_file_obj = open("api_keys.txt", "r")
    alpaca_keys = parse_keys(alpaca_file_obj)

    polygon_file_obj = open("polygon_keys.txt", "r")
    polygon_keys = parse_keys(polygon_file_obj)

    # setting this up for a paper trading account
    trade_url = "https://paper-api.alpaca.markets"

    # ayment is required to use Polygon streaming API
    data_url = "wss://alpaca.socket.polygon.io/stocks"

    # Use the REST API using the keys from Alpaca and the paper trading site
    api = trade_api.REST(
        alpaca_keys["key"], alpaca_keys["secret"], trade_url, api_version="v2"
    )

    # establish the data streaming connection
    connection = StreamConn(polygon_keys["key"], polygon_keys["secret"], data_url)

    # create the trading bot object with the api and stream and run it
    trade_bot = TradingBot(api, connection)
    trade_bot.run()

    return None


if __name__ == "__main__":
    main()
