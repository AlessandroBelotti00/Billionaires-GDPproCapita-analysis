from import_file import *

def european_GDP_def():
    # source -> https://ec.europa.eu/eurostat/databrowser/view/nama_10r_2gvagr/default/table?lang=en

    region_GDP = pd.read_csv("./original_data/european_GDP_procapite.csv")
    region_GDP = region_GDP[['TIME', '2014','2015','2016','2017','2018','2019','2020','2021']][1:]
    region_GDP

    ## Dataset related to European countries GDP (European_GDP_procapite.csv)
    # HERE THE EUROPEAN PRO CAPITA GDP CURRENCY IS TRANSLATED FROM EURO INTO USD AT CURRENT CHANGE VALUE
    change_val = 1.0804
    cont = 1

    for j in region_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
        list=[]
        for i in region_GDP[j]:
            tmp=i.replace(',','.')
            #print(round(float(i)*1000.0, 2))
            if tmp.strip() != ':':
                list.append(round(float(tmp)*1000.0, 2))
            else:
                list.append(0.0)
                
        region_GDP[j]=list

    # HERE THE EUROPEAN PRO CAPITA GDP CURRENCY IS TRANSLATED FROM THOUSANDS OF USD TO USD
    for j in region_GDP[['2014','2015','2016','2017','2018','2019','2020','2021']]:
        list=[]
        for i in region_GDP[j]:
            if i==':':
                i=i.replace(i,'0')
                list.append(i)
            else:
                i=i*change_val
                list.append(i)
        
        region_GDP[j]=list

    # mean replacement of null values
    lista=[]
    for i in region_GDP.iterrows():
        if i[1]['2014']>=2 and i[1]['2015']>=2 and i[1]['2016']>=2 and i[1]['2017']>=2 and i[1]['2018']>=2 and i[1]['2019']>=2 and i[1]['2020']>=2 and i[1]['2021']>=2:
            lista.append({"Country Name":i[1]['TIME'], "2014":i[1]['2014'], "2015":i[1]['2015'], "2016":i[1]['2016'], "2017":i[1]['2017'] ,"2018":i[1]['2018'] ,"2019":i[1]['2019'],"2020":i[1]['2020'], "2021":i[1]['2021'],})        
        else:
            if i[1]['2014']>=2 or i[1]['2015']>=2 or i[1]['2016']>=2 or i[1]['2017']>=2 or i[1]['2018']>=2 or i[1]['2019']>=2 or i[1]['2020']>=2 or i[1]['2021']>=2:
                lista_valori = [i[1]['2014'],i[1]['2015'],i[1]['2016'],i[1]['2017'],i[1]['2018'],i[1]['2019'],i[1]['2020'],i[1]['2021']]
                media = np.mean([valore for valore in lista_valori if valore>2])
                lista_valori_sostituiti = pd.Series(lista_valori).fillna(media).tolist()
                lista.append({"Country Name":i[1]['TIME'], "2014":lista_valori_sostituiti[0],"2015":lista_valori_sostituiti[1],"2016":lista_valori_sostituiti[2],"2017":lista_valori_sostituiti[3],"2018":lista_valori_sostituiti[4],"2019":lista_valori_sostituiti[5],"2020":lista_valori_sostituiti[6],"2021":lista_valori_sostituiti[7]})

    return region_GDP