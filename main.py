import alpaca_trade_api as trade_api 
import time

def parse_keys(file_obj): 
    keys_dict = {} 

    for line in file_obj: 
        line_list = line.split(":")
        keys_dict[line_list[0]] = line_list[1].strip("\n")

    return keys_dict


def main(): 
    file_obj = open("api_keys.txt", "r")
    keys_dict = parse_keys(file_obj)

    url = "https://paper-api.alpaca.markets"

    api = trade_api.REST(keys_dict["key"], keys_dict["secret"], url, api_version="v2")

    account = api.get_account() 

    print(account.status)

    pass

if __name__ == "__main__": 
    main() 
