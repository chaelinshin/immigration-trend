#%%
# Change xlsx files to csv 

# based on codes from https://www.marsja.se/how-to-convert-json-to-excel-python-pandas/ (retrieved 11/01/2020)
import pandas as pd 
df = pd.read_excel('Data/US_refugee/fy2019_table13.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USrefugeeTotal.csv')

#%%
df = pd.read_excel('Data/US_refugee/fy2019_table16.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USasylum.csv')

#%%
df = pd.read_excel('Data/US_greencard_region_country.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USgreencardByRegionCountry.csv')

#%%
df = pd.read_excel('Data/US_apprehension/fy2019_table33.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USapprehend.csv')

#%%
df = pd.read_excel('Data/US_apprehension/fy2019_table36.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USinadmissibleAlien.csv')

#%%
df = pd.read_excel('Data/US_apprehension/fy2019_table39.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USRemovedReturnedAlien.csv')

#%%
df = pd.read_excel('Data/US_greencard/fy2019_table1.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USgreencardTotal.csv')

#%%
df = pd.read_excel('Data/US_nonimmigrant/fy2019_table25d.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/Final Project/Data/csv/USnonimmigrantbyCategory.csv')

# %%

df = pd.read_excel(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/US_greencard/fy2019_table3d.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/USGreencardOrigin.csv')

# %%
df = pd.read_excel(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/US_greencard/fy2019_table4.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/USGreencardState.csv')

# %%
df = pd.read_excel(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/US_refugee/fy2019_table14d.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/USRefugeeOrigin.csv')

# %%
df = pd.read_excel(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/US_nonimmigrant/fy2019_table26.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/USNonimmigrantOrigin.csv')
# %%
df = pd.read_excel(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/US_nonimmigrant/fy2019_table30.xlsx')
df.to_csv(r'C:/Users/chael/Desktop/Visualization/FinalProject/Data/csv/USNonimmigrantState.csv')

