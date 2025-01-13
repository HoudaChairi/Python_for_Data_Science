
def NULL_not_found(object: any) -> int:
    """
    Evaluates the given object and prints a message based on specific conditions:

    - "Nothing" for `None`.
    - "Cheese" for NaN (float).
    - "Zero" for the integer 0.
    - "Empty" for empty strings.
    - "Fake" for the boolean value False.
    - Prints "Type not Found" if none of the conditions are met and returns 1.

    Returns:
    - 0 if a matching condition is found.
    - 1 if no condition is met.
    """
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