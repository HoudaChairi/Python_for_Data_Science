
def ft_filter(function, element):
    """
    Filters 'element' based on 'function'.
    If no function, returns truthy elements.

    Parameters:
    function: Function to filter elements.
    element: Iterable to filter.

    Returns:
    List of filtered elements.
    """
    if function is not None:
        return [x for x in element if function(x)]
    return [x for x in element if x]

    # example:
    # new_list = []
    # for x in element:
    #     if function(x):
    #         new_list.add(x)
    # return new_list
