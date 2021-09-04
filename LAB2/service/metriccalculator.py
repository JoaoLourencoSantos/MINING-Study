
import pandas as pd


def generateMetrics():
    try:
        dataset = pd.read_csv('./project/class.csv')
        dataset.head()

        # Calculate Median of 'Fare' column
        cbo = dataset['cbo'].median()
        dit = dataset['dit'].median()
        loc = dataset['loc'].sum()
        lcom = dataset['lcom'].median()

        return {
            "cbo": cbo,
            "dit": dit,
            "lcom": lcom,
            "loc": loc
        }

    except:
        print(' [*] Error on read statistics file!')
