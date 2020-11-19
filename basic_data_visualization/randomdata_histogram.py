
## import libraries ##
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

## randomly generate data ##
np.random.seed(35)
x = np.random.normal(size=4000)

## set up histogram ##
bins = np.linspace(0, 2, 40)
plt.hist(x, density=True, bins=30, histtype='bar', ec='black', label="Data")
mn, mx = plt.xlim()
plt.xlim(mn, mx)
kde_xs = np.linspace(mn, mx, 301)
kde = st.gaussian_kde(x)
plt.plot(kde_xs, kde.pdf(kde_xs), label="Distribution")
plt.legend(loc="upper left")
plt.ylabel('Frequency')
plt.xlabel('Classes')
plt.title("Histogram");
plt.grid()

## display histogram ##
plt.show()

