

def ft_tqdm(lst: range) -> None:
    """
    Displays a progress bar while iterating over the given iterable.

    Args:
        lst (range): The iterable to loop through.

    Yields:
        item: The current item in the iteration.
    """
    total = len(lst)
    count = 0
    for item in lst:
        count += 1
        percent = (count / total) * 100
        bar = '=' * int(percent // 2)
        spaces = ' ' * (50 - len(bar))

        print(f'\r[{bar}{spaces}] {percent:.2f}% \
        ({count}/{total})', end='', flush=True)

        yield item
    print()
