
#well we should use some built-in function to check the data type of entered value or information.

def typeBasedTransformer(**Alex):
    for name, value in Alex.items():
        if isinstance(value, (int, float)):  #I used isinstance becuase using type() function doesnt allow me to check two types  once.
            print(f"{name}: {value ** 2}")
        elif isinstance(value, str):          
            print(f"{name}: {value[::-1]}")
        elif isinstance(value, bool):
            print(f"{name}: {not value}")
        elif isinstance(value, (list, tuple)):
            print(f"{name}: {value[::-1]}")
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value.values()):
                print(f"{name}: {{ {', '.join(f'{v}: {k}' for k, v in value.items())} }}")
            else:
                print(f"{name}: {value}") 
        else:
            print(f"{name}: {value}") 


# typeBasedTransformer(name="Asilbek", age=19, city="Tashkent", occupation="Student", electricity = True, heights = [178, 183, 190])
