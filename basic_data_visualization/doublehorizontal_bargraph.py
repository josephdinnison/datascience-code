
## import libraries ##
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## import data ##
doublehorizontal_data = pd.read_csv(r'C:\Users\Joey261\Desktop\Career\datascience3_stratified.csv')
bar_width = 0.3
bar_heightmale = doublehorizontal_data['Male']
bar_heightfemale = doublehorizontal_data['Female']
x_values = doublehorizontal_data['Movie Preference']
x = np.arange(len(x_values))

## display tabular data ##
print(doublehorizontal_data)


## set up bar chart ##
doublehorizontal_data.plot(kind='barh')
plt.xlabel('Number of People')
plt.ylabel('Favorite Movie Genre')
plt.yticks([0,1,2,3], ['Action', 'Horror', 'Comedy', 'Romance'])
plt.title('Favorite Movie Genres')
plt.legend()

## display bar chart ##
plt.show()


