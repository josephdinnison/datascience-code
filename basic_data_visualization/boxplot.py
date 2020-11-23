
## import libraries ##
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## import and format data from Excel ##
boxandwhiskers_data = pd.read_csv(r'C:\Users\Joey261\Desktop\Career\datascience6_boxandwhisker.csv', header=None)
column_to_drop = [0]
boxandwhiskers_data.drop(column_to_drop, inplace=True, axis=1)

## convert dataframe to list ##

testscores = list(boxandwhiskers_data.values.flatten())

scores_2016 = testscores[0:15]
scores_2017 = testscores[15:30]
scores_2018 = testscores[30:45]
scores_2019 = testscores[45:60]
scores_2020 = testscores[60:75]

scores_list = [scores_2016, scores_2017, scores_2018, scores_2019, scores_2020]
x_values_list = []

## label and display plot ##
fig, ax1 = plt.subplots()
ax1.set_title('Test Scores (2016-2020)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Scores')
plt.xticks(x_values_list, ['2016', '2017', '2018', '2019', '2020'])
bp = plt.boxplot(scores_list)
plt.show()
