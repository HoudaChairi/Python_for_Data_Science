import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        life_expectancy = load(
            'life_expectancy_years.csv'
        )
        gdp = load(
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        )

        life_1900 = life_expectancy[['1900']].dropna()
        gdp_1900 = gdp[['1900']].dropna()

        combined = life_1900.join(
            gdp_1900, how='inner', lsuffix='_life', rsuffix='_gdp'
        )
        combined.columns = ['Life Expectancy', 'GDP']

        plt.figure(figsize=(8, 6))
        plt.scatter(
            combined['GDP'], combined['Life Expectancy'],
            alpha=0.7, edgecolors='b'
        )
        plt.xscale('log')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.show()

    except Exception as e:
        print(type(e).__name__, ":", e)


if __name__ == '__main__':
    main()
