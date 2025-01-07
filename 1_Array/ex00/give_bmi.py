import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates BMI for a list of heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """
    try:
        if (len(height) != len(weight)):
            raise AssertionError("the arguments are bad")

        for i in range(len(height)):
            if (
                type(height[i]) not in [int, float]
                or type(weight[i]) not in [int, float]
            ):
                raise AssertionError("the arguments are bad")

        np_height = np.array(height, dtype=np.float64)
        np_weight = np.array(weight, dtype=np.float64)

        calcul_bmi = np_weight / (np_height ** 2)
        return calcul_bmi.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a BMI limit filter and returns a list indicating
    if each BMI exceeds the limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The BMI limit for comparison.

    Returns:
        list[bool]: List of boolean values indicating
        if each BMI exceeds the limit.
    """
    try:
        if (type(limit) is not int):
            raise AssertionError("the arguments are bad")
        for i in range(len(bmi)):
            if (type(bmi[i]) not in [int, float]):
                raise AssertionError("the arguments are bad")

        numpy_list = np.array(bmi)
        return (numpy_list > limit).tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
