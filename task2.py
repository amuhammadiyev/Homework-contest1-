
def typeBasedTransformer(**Alex):
    for name, value in Alex.items():
        if type(value) == int or type(value) == float:
            print(f"{name}: {value ** 2}")
        elif type(value) == str:
            print(f"{name}: {value[::-1]}")
        elif type(value) == bool:
            print(f"{name}: {not value}")
        elif type(value) == list or type(value) == tuple:
            print(f"{name}: {value[::-1]}")
        elif type(value) == dict:
            reversed_dict = {}
            for k, v in value.items():
                reversed_dict[v] = k
            print(reversed_dict)
        else:
            print(f"{name}: {value}") 
