import pandas

dat = pandas.read_csv('data/gapminder_all.csv')

dat['lifeExp_2007'].max()
