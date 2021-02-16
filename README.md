Using Selenium, I was able to scrape 2 websites of lab diamond retailers, Clean Origin and MiaDonna. Using that data along with ggplot's diamond dataset, I was able to perform comparative analysis between the two types of diamonds. Results are showcased using various Python packages, graphed with Seaborn.

Diamonds used for engagement rings were my main focus. Although diamonds of various carat weights are used, I focused on the average diamond sizes used for proposals (between 1.08 and 1.2), and broadened the range to 0.5 to 2.5 carats for the general audience.

All the diamonds in the dataset are round-cut, to be consistent with the ggplot diamonds dataset. Other variables will vary along the industry scales of color, cut, and clarity:

Variable scales from best to worst:
Cut: Ideal / Excellent / Very Good / Good / Fair / Poor
Clarity: IF / VVS1 / VVS2 / VS1 / VS2 / SI1 / SI2 / I1
Color: D / E / F / G / H / I / J / K

After finding the strong correlation between price and carat weight, I created the "Price-per-Carat" variable to normalize the data while comparing across other variables. The column is titled "ppc."
