
## import libraries ##
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors
import numpy as np

## import data and set variables ##
histogram_data = pd.read_csv(r'C:\Users\Joey261\Desktop\Career\datascience2.csv')
pie_values = histogram_data['PERCENT OF PEOPLE']
label_values = histogram_data['FAVORITE MOVIE TYPE']
explode = (0.0, 0.1, 0.0, 0.0, 0.0, 0.0)


## display tabular data ##
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(histogram_data)

## create autocpt arguments(percents to label pie wedges) ##
def func(pct, allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return "{:.1f}%\n".format(pct, absolute)

## set up pie chart ##
plt.pie(pie_values, explode=explode, labels=label_values,
        autopct= lambda pct: func(pct, pie_values), shadow=True)
plt.title('Movies Bar Graph')



## display pie chart ##
plt.axis('equal')
plt.show()

