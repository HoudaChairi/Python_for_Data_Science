
def all_thing_is_obj(object: any) -> int:
    """
    This function checks the type of a given object and prints its type:

    - Recognized types: list, tuple, set, dict, and str.
    - For strings, a custom message is displayed with the object value.
    - Prints "Type not found" for unrecognized types.
    - Always returns the integer 42.

    Parameters:
    - object: Any Python object to check its type.

    Returns:
    - int: Always returns 42.
    """

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
