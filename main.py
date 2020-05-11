import time
import matplotlib.pyplot as plt 
import numpy as np 
import alpaca_trade_api as trade_api 

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
    url = "https://paper-api.alpaca.markets"

    # Use the REST API using the keys from Alpaca and the paper trading site 
    api = trade_api.REST(keys_dict["key"], keys_dict["secret"], url, api_version="v2")

    # get access to the account using the credentials 
    account = api.get_account() 

    return None 

if __name__ == "__main__": 
    main() 
