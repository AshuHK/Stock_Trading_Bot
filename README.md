# Stock_Trading_Bot
 Building a simple trading bot using the Alpaca Trading API
  - Can only trade a single stock at a time
    - The method in this program uses the Doji candle to decide when to buy and sell (sells at 1 percent profit) 
  - Just simply change the stock ticker symbol to specify which stock to trade
    - Requires an account at alpaca.markets and polygon.io (payment required)
      - alpaca.markets: trading platform and API
      - polygon.io: data stream API that gets real time stock prices and other data
