#%% 
import pandas as pd 
import os

#%%
# clean 'USrefugeetotal.csv': from years 2009 to 2019
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/')
path = os.getcwd()
filepath = os.path.join(path, 'USrefugeeTotal.csv')
USrefugeedf = pd.read_csv(filepath, skiprows=3)

# remove unnecessary columns
USrefugeedf = USrefugeedf.drop(USrefugeedf.columns[[0]], axis=1)

# remove unnecessary rows
USrefugeedf = USrefugeedf.drop(USrefugeedf.index[0:29])

# reset index and remove rows
USrefugeedf.index = pd.RangeIndex(start=0, stop=13, step=1)

USrefugeedf = USrefugeedf.drop(index=[11,12])

# save cleaned file as 'cleanUSRefugee.csv'
USrefugeedf.to_csv('cleanUSRefugee.csv')

# %%
# clean 'USgreencardTotal.csv': from years 2009 to 2019
filepath = os.path.join(path, 'USgreencardTotal.csv')
USgreendf = pd.read_csv(filepath, skiprows=3)

# remove unnecessary elements
USgreendf = USgreendf.drop(USgreendf.iloc[0:50, 1:7], axis=1)
USgreendf = USgreendf.drop(USgreendf.columns[[0]], axis=1)

# remove unnecessary rows
USgreendf = USgreendf.drop(USgreendf.index[0:39])

# reset index and remove rows
USgreendf.index = pd.RangeIndex(start=0, stop=13, step=1)
USgreendf = USgreendf.drop(index=[11,12])

# rename columns
USgreendf.columns = ['Year', 'Number']

# save cleaned file as 'cleanUSGreenCard.csv'
USgreendf.to_csv('cleanUSGreenCard.csv')

# %%
# clean 'USapprehend.csv': from years 2009 to 2019
filepath = os.path.join(path, 'USapprehend.csv')
USappdf = pd.read_csv(filepath, skiprows=3)

# remove unnecessary elements
USappdf = USappdf.drop(USappdf.iloc[0:56, 1:3], axis=1)
USappdf = USappdf.drop(USappdf.columns[[0]], axis=1)

# remove unnecessary rows
USappdf = USappdf.drop(USappdf.index[0:28])

# resent index and remove rows
USappdf.index = pd.RangeIndex(start=0, stop=34, step=1)
USappdf = USappdf.drop(USappdf.index[11:34])

# rename columns
USappdf.columns = ['Year', 'Number']

# edit elements
USappdf.iloc[0, 0] = 2009
USappdf.iloc[7, 0] = 2016

# save cleaned file as 'cleanUSApprehend.csv'
USappdf.to_csv('cleanUSApprehend.csv')

# %%
# clean 'USRemovedReturnedAlien.csv': from years 2009 to 2019
filepath = os.path.join(path, 'USRemovedReturnedAlien.csv')
USremovedf = pd.read_csv(filepath, skiprows=3)

# remove unnecessary columns
USremovedf = USremovedf.drop(USremovedf.columns[[0]], axis=1)

# remove unnecessary rows
USremovedf = USremovedf.drop(USremovedf.index[0:117])

# reset index
USremovedf.index = pd.RangeIndex(start=0, stop=17, step=1)

# remove rows
USremovedf = USremovedf.drop(USremovedf.index[11:17])

# remove columns
USremovedf = USremovedf.drop(USremovedf.columns[[3,4]], axis=1)

# rename columns
USremovedf.columns = ['Year', 'Removals', 'Returns']

USremovedf.iloc[7,0] = 2016

# save cleaned file as 'cleanUSRemoveReturn.csv'
USremovedf.to_csv('cleanUSRemoveReturn.csv')

# %%
# clean 'RefugeeByCountryofAsylum.csv': from years 2009 to 2019
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/')
path = os.getcwd()
filepath = os.path.join(path, 'RefugeeByCountryofAsylum.csv')
asylum_df = pd.read_csv(filepath, skiprows=4)

# drop columns
asylum_df = asylum_df.drop(asylum_df.iloc[:, 1:53], axis=1)
asylum_df = asylum_df.drop(asylum_df.columns[[12]], axis=1)

# G20
asylum_df = asylum_df[asylum_df['Country Name'].isin(['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'Japan', 'Korea, Rep.', 'Mexico', 'Saudi Arabia', 'South Africa', 'Turkey', 'United Kingdom', 'United States'])]

# create "Total" column
asylum_df["Total"] = asylum_df['2009'].fillna(0) + asylum_df['2010'].fillna(0) + asylum_df['2011'].fillna(0) + asylum_df['2012'].fillna(0) + asylum_df['2013'].fillna(0) + asylum_df['2014'].fillna(0) + asylum_df['2015'].fillna(0) + asylum_df['2016'].fillna(0) + asylum_df['2017'].fillna(0) + asylum_df['2018'].fillna(0) + asylum_df['2019'].fillna(0)

# reset index
asylum_df.index = pd.RangeIndex(start=0, stop=18, step=1)   

# rename
asylum_df.iloc[[12], [0]] = 'South Korea'

# save cleaned file
asylum_df.to_csv('cleanRefugeebyCountryofAsylum.csv')
# %%
# clean 'RefugeeByCountryofOrigin.csv'
filepath = os.path.join(path, 'RefugeeByCountryofOrigin.csv')
origin_df = pd.read_csv(filepath, skiprows=4)

# drop columns
origin_df = origin_df.drop(origin_df.iloc[:, 1:53], axis=1)
origin_df = origin_df.drop(origin_df.columns[[12,13]], axis=1)

# create "Total" column
origin_df["Total"] = origin_df['2009'].fillna(0) + origin_df['2010'].fillna(0) + origin_df['2011'].fillna(0) + origin_df['2012'].fillna(0) + origin_df['2013'].fillna(0) + origin_df['2014'].fillna(0) +origin_df['2015'].fillna(0) + origin_df['2016'].fillna(0) + origin_df['2017'].fillna(0) + origin_df['2018'].fillna(0) + origin_df['2019'].fillna(0)

origin_df = origin_df[origin_df['Total'] > 0]

# remove rows that are not countries
origin_df = origin_df[~origin_df['Country Name'].isin(['Early-demographic dividend', 'Arab World','Fragile and conflict affected situations', 'High Income', 'Heavily indebted poor countries (HIPC)', 'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only', 'Least developed countries: UN classification', 'Lower middle income', 'Low income', 'Low & middle income', 'Late-demographic dividend', 'OECD members', 'Other small states', 'Pre-demographic dividend', 'Post-demographic dividend', 'Small states', 'Upper middle income', 'World'])]


# change names
origin_df['Country Name'] = origin_df['Country Name'].replace(['Korea, Rep.'],'South Korea')
origin_df['Country Name'] = origin_df['Country Name'].replace(['Syrian Arab Republic'], 'Syria')
origin_df.iloc[[155], [0]] = 'North Korea'

# save cleaned file
origin_df.to_csv('cleanRefugeebyCountryofOrigin.csv')
# %%
# clean 'Population.csv'

filepath = os.path.join(path, 'Population.csv')
popdf = pd.read_csv(filepath, skiprows=4)

# Choose U.S.
popdf = popdf[popdf['Country Name'] == 'United States']

# drop columns
popdf = popdf.drop(popdf.iloc[:, 1:53], axis=1)
popdf = popdf.drop(popdf.columns[[12,13]], axis=1)

# change dataframe to list
poplist = popdf.values.tolist()
poplist = poplist[0]
poplist.remove('United States')

#%%
# bring 'cleanUSRefugee.csv'
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/cleaned/')
path = os.getcwd()
filepath = os.path.join(path, 'cleanUSRefugee.csv')
USref = pd.read_csv(filepath)

USref = USref.drop(USref.columns[[0]], axis=1)

# get percentage : (# of refugees) / (total population) * 100
USreflist = USref["Number"].values.tolist()

refratio = [(ref / pop) * 100 for ref, pop in zip(USreflist, poplist)]

# add "Percentage" column to dataframe
USref['Percentage'] = refratio

# add "Population" column to dataframe
USref['Population'] = poplist

# save new dataframe 
USref.to_csv('cleanUSRefugeeAndPopulation.csv')
# %%
# load 'cleanUSApprehend.csv'
filepath = os.path.join(path, 'cleanUSApprehend.csv')
appdf = pd.read_csv(filepath)

# remove unnecessary column
appdf = appdf.drop(appdf.columns[[0]], axis=1)

# make list
applist = appdf['Number'].values.tolist()

# %%
# load 'cleanUSRemoveReturn.csv'
filepath = os.path.join(path, 'cleanUSRemoveReturn.csv')
returndf = pd.read_csv(filepath)

# remove unnecessary column
returndf = returndf.drop(returndf.columns[[0]], axis=1)

# add 'Apprehend' column
returndf['Apprehend'] = applist

# save cleaned file
returndf.to_csv('cleanUSRemoveReturnApprehend.csv')
# %%
# bring nonimmigrant data
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/')
path = os.getcwd()
filepath = os.path.join(path, 'USnonimmigrantbyCategory.csv')
nonim = pd.read_csv(filepath, skiprows=3)

# select categories of interest
nonim = nonim[nonim['Class of admission'].isin(['Total all admissions1', 'Temporary workers in specialty occupations (H1B)', 'Academic students (F1)']) ]

# make lists
nonimmigrant_list = nonim.values.tolist()
total_list = nonimmigrant_list[0]
H1B_list = nonimmigrant_list[1]
F1_list = nonimmigrant_list[2]

total_list.remove(3)
total_list.remove('Total all admissions1')

H1B_list.remove(9)
H1B_list.remove('Temporary workers in specialty occupations (H1B)')

F1_list.remove(40)
F1_list.remove('Academic students (F1)')
# %%
# bring 'cleanUSGreenCard.csv'
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/cleaned/')
path = os.getcwd()
filepath = os.path.join(path, 'cleanUSGreenCard.csv')
greendf = pd.read_csv(filepath)

# remove unnecessary column
greendf = greendf.drop(greendf.columns[[0]], axis=1)

# rename column 'Number' to 'GreenCard'
greendf.columns = ['Year', 'GreenCard']

# remove year 2009 
greendf = greendf[greendf['Year'] > 2009]

# add lists to dataframe
greendf['H1B'] = H1B_list
greendf['F1'] = F1_list

# save as 'cleanUSGreencardNonimmigrant.csv'
greendf.to_csv('cleanUSGreencardNonimmigrant.csv')

# %%
# bring 'USGreencardOrigin.csv'
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/')
path = os.getcwd()
filepath = os.path.join(path, 'USGreencardOrigin.csv')
greendf = pd.read_csv(filepath, skiprows=3)

# select region
greendf = greendf[greendf['Region and country of birth'].isin(['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown'])]

# drop columns
greendf = greendf.drop(greendf.columns[[0]], axis=1)

# select rows
greendf = greendf[:7]

# transpose
greendf = greendf.transpose()

# set index
greendf.index = pd.RangeIndex(start=0, stop=11, step=1)

# shift row
greendf = greendf.shift(-1)

# name columns
greendf.columns = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown']

# select rows
greendf = greendf[:10]

# insert "Year" column
yearlist = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
greendf.insert(loc=0, column="Year", value=yearlist)

# save cleaned file
greendf.to_csv('cleanUSGreencardOrigin.csv')
# %%
# clean 'USGreencardState.csv'
filepath = os.path.join(path, 'USGreencardState.csv')
greendf = pd.read_csv(filepath, skiprows=3)

# remove column
greendf = greendf.drop(greendf.columns[[0]], axis=1)

# select rows
greendf = greendf[1:56]

# rename
greendf.iloc[[53], [0]] = 'Other'

# rename columns
greendf.columns = ['State', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

# save cleaned file
greendf.to_csv('cleanUSGreencardState.csv')

# %%
# bring 'USRefugeeOrigin.csv'
# os.chdir('C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/')
path = os.getcwd()
filepath = os.path.join(path, 'USRefugeeOrigin.csv')
refdf = pd.read_csv(filepath, skiprows=3)

# select region
refdf = refdf[refdf['Region and country of nationality'].isin(['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown'])]

# drop column
refdf = refdf.drop(refdf.columns[[0]], axis=1)

# select rows
refdf = refdf[:7]

# transpose
refdf = refdf.transpose()

# set index
refdf.index = pd.RangeIndex(start=0, stop=11, step=1)

# shift row
refdf = refdf.shift(-1)

# name columns
refdf.columns = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown']

# select rows
refdf = refdf[:10]

# add 'Year' column
yearlist = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
refdf.insert(loc=0, column="Year", value=yearlist)

# take care of null values
refdf['Oceania'] = [0, 0, 0, 0, 0, 0, 0, 0, 5, 0]
refdf.iloc[[8], [7]] = 0

# save cleaned file
refdf.to_csv('cleanUSRefugeeOrigin.csv')
# %%
# clean 'USNonimmigrantOrigin.csv'
filepath = os.path.join(path, 'USNonimmigrantOrigin.csv')
nondf = pd.read_csv(filepath, skiprows=3)

# select region
nondf = nondf[nondf['Region and country of citizenship'].isin(['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown'])]

# drop column
nondf = nondf.drop(nondf.columns[[0]], axis=1)

# select rows
nondf = nondf[:7]

# transpose
nondf = nondf.transpose()

# set index
nondf.index = pd.RangeIndex(start=0, stop=11, step=1)

# shift row
nondf = nondf.shift(-1)

# name columns
nondf.columns = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Unknown']

# select rows
nondf = nondf[:10]

# add "Year" column
yearlist = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
nondf.insert(loc=0, column="Year", value=yearlist)

# save cleaned file
nondf.to_csv("cleanUSNonimmigrantOrigin.csv")
# %%
# clean 'USNonimmigrantState.csv'
filepath = os.path.join(path, 'USNonimmigrantState.csv')
nondf = pd.read_csv(filepath, skiprows=3)

# drop columns
nondf = nondf.drop(nondf.columns[[0]], axis=1)
nondf = nondf.drop(nondf.iloc[:, 2:10], axis=1)

# select rows
nondf = nondf[2:55]

# name columns
nondf.columns = ['State', 'Total']

# save cleaned file
nondf.to_csv('cleanUSNonimmigrantState.csv')
