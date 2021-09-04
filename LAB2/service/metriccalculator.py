
from jar.execute import produceMetrics
import pandas as pd
import math


def generateMetrics():

    try:

        produceMetrics()

        dataset = pd.read_csv('./jar/metrics/class.csv')
        dataset.head()

        # Calculate Median of 'Fare' column
        cbo = dataset['cbo'].median()
        dit = dataset['dit'].median()
        loc = dataset['loc'].sum()
        lcom = dataset['lcom'].median()

        return {
            "cbo": cbo if cbo and not math.isnan(cbo) else "0",
            "dit": dit if dit and not math.isnan(dit) else "0",
            "lcom": lcom if lcom and not math.isnan(lcom) else "0",
            "loc": loc if loc and not math.isnan(loc) else "0"
        }

    except:
        print(' [*] Error on read statistics file!')
