import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a dataset from the given file path,
    prints its dimensions, and returns it.

    Parameters:
    path (str): The file path to the dataset.

    Returns:
    pd.DataFrame: The loaded dataset as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(path, index_col='country')

        print(f"Loading dataset of dimensions {data.shape}")

        return data
    except AssertionError as e:
        print(f"AssertionError: {e}")
