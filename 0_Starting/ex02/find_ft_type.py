
def all_thing_is_obj(object: any) -> int: 
    
    type_name = type(object)

    if type_name == list:
        print("List : ", type_name)
    elif type_name == tuple:
        print("Tuple : ", type_name)
    elif type_name == set:
        print("Set : ", type_name)
    elif type_name == dict:
        print("Dict : ", type_name)
    elif type_name == str:
        print(f"{object} is in the kitchen : ", type_name)
    else:
        print("Type not found")
        
    return (42)