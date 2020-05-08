
def parse_keys(file_obj): 
    keys_dict = {} 
    for line in file_obj: 
        # print(line)
        line_list = line.split(":")
        
        keys_dict[line_list[0]] = line_list[1]

        # print(line_list)

    return keys_dict


def main(): 
    file_obj = open("api_keys.txt", "r")
    
    keys_dict = parse_keys(file_obj)
    
    print(keys_dict)

    pass

if __name__ == "__main__": 
    main() 
