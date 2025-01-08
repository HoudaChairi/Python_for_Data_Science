from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def convert_population(value):
    """
    Converts a population string with 'M' (millions) or 'K' (thousands)
    suffixes into a float.
    Assumes plain numeric values if no suffix is present.
    """
    value = str(value).strip().upper()
    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    elif value.endswith('K'):
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def main():
    """
    Plots population projections for two countries using historical data.
    """
    try:
        df = load("population_total.csv").T

        country = 'Morocco'
        other_country = 'France'

        if country in df.columns and other_country in df.columns:

            df[country] = df[country].apply(convert_population)
            df[other_country] = df[other_country].apply(convert_population)

            df.index = df.index.astype(int)

            years = np.arange(1800, 2050, 40)
            df_filtered = df[df.index.isin(years)]

            plt.figure(figsize=(8, 4))
            df_filtered[country].plot(
                label=country,
                xlabel='Year',
                ylabel='Population',
                title='Population Projections'
            )
            df_filtered[other_country].plot(label=other_country)

            ticks = np.arange(1800, 2050, 40)
            plt.xticks(ticks, labels=[str(year) for year in ticks])
            plt.xticks(rotation=45)

            plt.legend()
            plt.show()

        else:
            print(
                f"One or both of the countries ({country}, {other_country}) "
                "not found in the dataset."
            )
    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
