 
def NULL_not_found(object: any) -> int:

    if object is None:
        print("Nothing:", f"{object}", type(object))
    elif (object != object and type(object) == float):
        print("Cheese:", f"{object}", type(object))
    elif (type(object) == int and object == 0):
        print("Zero:", f"{object}", type(object))
    elif (type(object) == str and not object):
        print("Empty:", type(object))
    elif type(object) == bool and object is False:
        print("Fake:", f"{object}", type(object))
    else:
        print("Type not Found")
        return (1)
    return (0)