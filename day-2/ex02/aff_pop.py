import matplotlib.pyplot as plt
from load_csv import load


def convert(value):

    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    if value.endswith('k'):
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def main():

    dataset = load("population_total.csv")
    country1 = "France"
    country2 = "Belgium"
    france_data = dataset[dataset['country'] == country1].iloc[:, 1:]
    belgium_data = dataset[dataset['country'] == country2].iloc[:, 1:]
    france_pop = france_data.values.flatten()
    belgium_pop = belgium_data.values.flatten()
    years = france_data.columns.astype(int).values
    france_pop = [convert(value) for value in france_pop]
    belgium_pop = [convert(value) for value in belgium_pop]
    plt.plot(years, france_pop, label=country1)
    plt.plot(years, belgium_pop, label=country2)
    plt.title("Population in {} and {} ".format(country1, country2))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(france_pop), max(belgium_pop))
    print(max(france_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()
