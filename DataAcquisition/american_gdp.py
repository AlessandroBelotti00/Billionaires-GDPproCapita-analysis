from import_file import *

def american_GDP_def():
    ## Dataset related to American GDP
    # source -> https://apps.bea.gov/itable/?ReqID=70&step=1&acrdn=1#eyJhcHBpZCI6NzAsInN0ZXBzIjpbMSwyNCwyOSwyNSwzMV0sImRhdGEiOltbIlRhYmxlSWQiLCI2MDAiXSxbIkNsYXNzaWZpY2F0aW9uIiwiTm9uLUluZHVzdHJ5Il0sWyJNYWpvcl9BcmVhIiwiMCJdXX0=
    USA_GDP = pd.read_csv("original_data/US_states_GDP.csv")
    USA_GDP=USA_GDP.drop(['GeoFips'], axis=1)

    # source -> https://www.census.gov/en.html
    USA_POP = pd.read_csv("./original_data/population_us.csv")
    print(USA_POP.shape[0])
    
    # From GDP to GDP per capita by dividing each value with the population of the year 2022.
    for j in USA_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
        list=[]
        cont = 0
        for i in USA_GDP[j][:52]:
            pop = USA_POP.iloc[cont]['2022_population']
            pop = pop.strip()        
            pop = pop.replace(",","")
            pop = pop.rstrip('.00')
            gdp_proCapite = round(float(i) / float(pop) * 1000000.0, 2)

            #print(f"{USA_POP.iloc[cont]['Country']} -> GDP: {gdp_proCapite} -> {float(i)}-->{j}>>>population:{float(pop)}")

            list.append(gdp_proCapite)
            cont += 1
            if cont >= USA_POP.shape[0]:

                break
        USA_GDP[j][:52]=list

    print(f"USA_GDP\n{USA_GDP.head(7)}\n")

    return USA_GDP