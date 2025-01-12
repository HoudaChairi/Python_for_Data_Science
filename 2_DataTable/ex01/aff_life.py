from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads life expectancy data and plots projections
    for a specified country (default: Morocco).

    The dataset is loaded using the `load()` function,
    and a line plot is generated to visualize the life
    expectancy over time. Error handling is included.
    """
    try:
        df = load("../ex00/life_expectancy_years.csv").T

        country = 'Morocco'
        df[country].plot(xlabel='Year', ylabel='Life expectancy',
                         title=f'{country} life expectancy projections')

        plt.show()

    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
