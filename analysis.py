import pandas

dat = pandas.read_csv('data/gapminder_all.csv')

dat['lifeExp_1992'].max()
