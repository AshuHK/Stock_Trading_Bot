
def parse_keys(file_obj): 

    for line in file_obj: 
        print(line)
    pass


def main(): 
    file_obj = open("api_keys.txt", "r")
    
    keys_dict = parse_keys(file_obj)

    pass

if __name__ == "__main__": 
    main() 
