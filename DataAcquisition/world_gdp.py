from import_file import *

def world_GDP_def():

    # source -> https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG
    world_GDP = pd.read_csv("./original_data/world_GDP.csv")
    world_GDP=world_GDP[['Country Name','2014','2015','2016','2017','2018','2019','2020','2021']]

    ## Dataset related to world countries per capita GDP (world_GDP.csv)
    # ROUND THE WORLD PRO CAPITA GDP AT TWO DECIMAL NUMBERS
    for j in world_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
        list=[]
        for i in world_GDP[j]:
            list.append(round(float(i), 2))
                
        world_GDP[j]=list

    # Country removing if there are all missing values for GDP from 2014 to 2021 and mean replacement for that countries which have at least one missing value but not all, must be 1 or more not null value.
    lista=[]
    for i in world_GDP.iterrows():
        if i[1]['2014']>=2 and i[1]['2015']>=2 and i[1]['2016']>=2 and i[1]['2017']>=2 and i[1]['2018']>=2 and i[1]['2019']>=2 and i[1]['2020']>=2 and i[1]['2021']>=2:
            lista.append({"Country Name":i[1]['Country Name'], "2014":i[1]['2014'], "2015":i[1]['2015'], "2016":i[1]['2016'], "2017":i[1]['2017'] ,"2018":i[1]['2018'] ,"2019":i[1]['2019'],"2020":i[1]['2020'], "2021":i[1]['2021'],})
        else:
            if i[1]['2014']>=2 or i[1]['2015']>=2 or i[1]['2016']>=2 or i[1]['2017']>=2 or i[1]['2018']>=2 or i[1]['2019']>=2 or i[1]['2020']>=2 or i[1]['2021']>=2:
                lista_valori = [i[1]['2014'],i[1]['2015'],i[1]['2016'],i[1]['2017'],i[1]['2018'],i[1]['2019'],i[1]['2020'],i[1]['2021']]
                media = np.mean([valore for valore in lista_valori if valore>2])
                lista_valori_sostituiti = pd.Series(lista_valori).fillna(media).tolist()
                lista.append({"Country Name":i[1]['Country Name'], "2014":lista_valori_sostituiti[0],"2015":lista_valori_sostituiti[1],"2016":lista_valori_sostituiti[2],"2017":lista_valori_sostituiti[3],"2018":lista_valori_sostituiti[4],"2019":lista_valori_sostituiti[5],"2020":lista_valori_sostituiti[6],"2021":lista_valori_sostituiti[7]})

    return world_GDP