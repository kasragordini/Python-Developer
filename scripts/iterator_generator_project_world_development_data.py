feature_names = ['CountryName',
 'CountryCode',
 'IndicatorName',
 'IndicatorCode',
 'Year',
 'Value']

row_vals = ['Arab World',
 'ARB',
 'Adolescent fertility rate (births per 1,000 women ages 15-19)',
 'SP.ADO.TFRT',
 '1960',
 '133.56090740552298']

# Zip lists
zipped_lists = zip(feature_names, row_vals)

# dictionary
rs_dict = dict(zipped_lists)

print(rs_dict)

### <script.py> output:
    {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}




def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists
    zipped_lists = zip(list1, list2)

    # dictionary
    rs_dict = dict(zipped_lists)

    return rs_dict

rs_fxn = lists2dict(feature_names, row_vals)

print(rs_fxn)

### output: {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}



# the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turning list of lists into list of dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]

print(list_of_dicts[0])
print(list_of_dicts[1])

###<script.py> output:
    ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']
    ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']
    {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}
    {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Age dependency ratio (% of working-age population)', 'IndicatorCode': 'SP.POP.DPND', 'Year': '1960', 'Value': '87.7976011532547'}

import pandas as pd

list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turning list of dicts into a DataFrame
df = pd.DataFrame(list_of_dicts)

print(df.head())

### <script.py> output:
      CountryName CountryCode                                      IndicatorName   IndicatorCode  Year               Value
    0  Arab World         ARB  Adolescent fertility rate (births per 1,000 wo...     SP.ADO.TFRT  1960  133.56090740552298
    1  Arab World         ARB  Age dependency ratio (% of working-age populat...     SP.POP.DPND  1960    87.7976011532547
    2  Arab World         ARB  Age dependency ratio, old (% of working-age po...  SP.POP.DPND.OL  1960   6.634579191565161
    3  Arab World         ARB  Age dependency ratio, young (% of working-age ...  SP.POP.DPND.YG  1960   81.02332950839141
    4  Arab World         ARB        Arms exports (SIPRI trend indicator values)  MS.MIL.XPRT.KD  1960           3000000.0




############# Now, We use the generator for streaming data

# Opening a connection to the file
with open('world_dev_ind.csv') as file:

    # Skipping the column names
    file.readline()

    counts_dict = {}

    for j in range(0, 1000):

        # Splitting the current line into a list
        line = file.readline().split(',')

        first_col = line[0]

        # This line increment the value if the column value is in the dict
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, adding to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)

### <script.py> output:
    {'Arab World': 80, 'Caribbean small states': 77, 'Central Europe and the Baltics': 71, 'East Asia & Pacific (all income levels)': 122, 'East Asia & Pacific (developing only)': 123, 'Euro area': 119, 'Europe & Central Asia (all income levels)': 109, 'Europe & Central Asia (developing only)': 89, 'European Union': 116, 'Fragile and conflict affected situations': 76, 'Heavily indebted poor countries (HIPC)': 18}





def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Looping indefinitely until the end of the file
    while True:

        data = file_object.readline()

        # Breaking if this is the end of the file
        if not data:
            break

        yield data
        
# Openning a connection to the file in conext manager
with open('world_dev_ind.csv') as file:

    # Creating a generator object for the file
    gen_file = read_large_file(file)

    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))


### <script.py> output:
    CountryName,CountryCode,IndicatorName,IndicatorCode,Year,Value
    
    Arab World,ARB,"Adolescent fertility rate (births per 1,000 women ages 15-19)",SP.ADO.TFRT,1960,133.56090740552298
    
    Arab World,ARB,Age dependency ratio (% of working-age population),SP.POP.DPND,1960,87.7976011532547





counts_dict = {}

with open('world_dev_ind.csv') as file:

    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)

### <script.py> output:
    {'CountryName': 1, 'Arab World': 80, 'Caribbean small states': 77, 'Central Europe and the Baltics': 71, 'East Asia & Pacific (all income levels)': 122, 'East Asia & Pacific (developing only)': 123, 'Euro area': 119, 'Europe & Central Asia (all income levels)': 109, 'Europe & Central Asia (developing only)': 89, 'European Union': 116, 'Fragile and conflict affected situations': 76, 'Heavily indebted poor countries (HIPC)': 99, 'High income': 131, 'High income: nonOECD': 68, 'High income: OECD': 127, 'Latin America & Caribbean (all income levels)': 130, 'Latin America & Caribbean (developing only)': 133, 'Least developed countries: UN classification': 78, 'Low & middle income': 138, 'Low income': 80, 'Lower middle income': 126, 'Middle East & North Africa (all income levels)': 89, 'Middle East & North Africa (developing only)': 94, 'Middle income': 138, 'North America': 123, 'OECD members': 130, 'Other small states': 63, 'Pacific island small states': 66, 'Small states': 69, 'South Asia': 36}


import pandas as pd

df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))

###                                  CountryName CountryCode                  IndicatorName      IndicatorCode  Year   Value
0                                 Arab World         ARB  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.285
1                     Caribbean small states         CSS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.597
2             Central Europe and the Baltics         CEB  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.508
3    East Asia & Pacific (all income levels)         EAS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  22.471
4      East Asia & Pacific (developing only)         EAP  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  16.918
5                                  Euro area         EMU  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.097
6  Europe & Central Asia (all income levels)         ECS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  55.379
7    Europe & Central Asia (developing only)         ECA  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  38.066
8                             European Union         EUU  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  61.213
9   Fragile and conflict affected situations         FCS  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  17.892
                                      CountryName CountryCode                  IndicatorName      IndicatorCode  Year   Value
10         Heavily indebted poor countries (HIPC)         HPC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  12.236
11                                    High income         HIC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.680
12                           High income: nonOECD         NOC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  56.108
13                              High income: OECD         OEC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  64.285
14  Latin America & Caribbean (all income levels)         LCN  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  49.285
15    Latin America & Caribbean (developing only)         LAC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.863
16   Least developed countries: UN classification         LDC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960   9.616
17                            Low & middle income         LMY  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  21.273
18                                     Low income         LIC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  11.498
19                            Lower middle income         LMC  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  19.811



# Initializing reader object
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Getting the first DataFrame chunk
df_urb_pop = next(urb_pop_reader)

print(df_urb_pop.head())

# Checking out specific country
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turning zip object into list
pops_list = list(pops)

print(pops_list)


### <script.py> output:
                                   CountryName CountryCode  Year  Total Population  Urban population (% of total)
    0                               Arab World         ARB  1960         9.250e+07                         31.285
    1                   Caribbean small states         CSS  1960         4.191e+06                         31.597
    2           Central Europe and the Baltics         CEB  1960         9.140e+07                         44.508
    3  East Asia & Pacific (all income levels)         EAS  1960         1.042e+09                         22.471
    4    East Asia & Pacific (developing only)         EAP  1960         8.965e+08                         16.918
    [(91401583.0, 44.5079211390026), (92237118.0, 45.206665319194), (93014890.0, 45.866564696018), (93845749.0, 46.5340927663649), (94722599.0, 47.2087429803526)]



# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

### output: plot



# Initializing reader object
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initializing empty DataFrame
data = pd.DataFrame()

# Iterating over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Checking out specific country
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turnning zip object into list
    pops_list = list(pops)

    # Using list comprehension to create new DataFrame column
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Concatenating DataFrame chunk to the end of data
    data = pd.concat([data, df_pop_ceb])

# Plotting urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


### output: plot



# Defining plot_pop()
def plot_pop(filename, country_code):

    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    data = pd.DataFrame()
    
    for df_urb_pop in urb_pop_reader:
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        pops_list = list(pops)

        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        
        data = pd.concat([data, df_pop_ceb])

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Setting the filename
fn = 'ind_pop_data.csv'

# Call plot_pop for country codes 'CEB' and 'ARB'
plot_pop('ind_pop_data.csv', 'CEB')
plot_pop('ind_pop_data.csv', 'ARB')


### output: plot


