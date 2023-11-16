import matplotlib.pyplot as plt
from load_csv import load

def main():
    dataset = load("life_expectancy_years.csv")
    
    
    france_data = dataset[dataset['country'] == 'France']
    years = france_data.columns[1:].values
    #print(years.values)
    life_expectancy = france_data.values[0][1:]
    #print(life_expectancy)

    plt.plot(years, life_expectancy, label='France')
    plt.title('Life expectancy in France from years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life expectancy')
    plt.yticks(range(30, 100, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()    

