
def ft_filter(function, element):
    if function is not None:
        return [x for x in element if function(x)]
    return [x for x in element if x]

    # example:
    # new_list = []
    # for x in element:
    #     if function(x):
    #         new_list.add(x)
    # return new_list
