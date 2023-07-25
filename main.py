from DataAcquisition.american_gdp import american_GDP_def
from DataAcquisition.world_gdp import world_GDP_def
from DataAcquisition.european_gdp import european_GDP_def
from DataAcquisition.worth_bill import worth_trend_scraping
from DataAcquisition.billionaires_forbes import import_true, add_continent, match_fixing
from mongoDB_preparation import *
from import_file import*

if __name__ == "__main__":
    # open all the raw datasets, if you want to re-run the scraping file you have to look at data_scraping.py
    
    """    world_GDP = world_GDP_def()
    region_GDP = european_GDP_def()
    USA_GDP = american_GDP_def()
    
    category_list = import_true()
    add_continent(category_list, USA_GDP)

    worth_trend = worth_trend_scraping(category_list)

    category_list = match_fixing(category_list,world_GDP) """

    # IF YOU WANT TO IMPORT THE PRE-RUNNED FILES RUN THESE
    ## Dataset related to bill characteristics (True.json)
    with open('exported_data/true.json', 'r', encoding='utf-8') as f:

        category_list = json.load(f)
    # first ten elements of the billionaires 
    cont = 0
    print("true.json\n")
    for el in category_list:
        if cont <= 1:
            print(el)
            cont += 1
    print("\n")


    ## Dataset related to world countries per capita GDP (world_GDP.csv)
    world_GDP = pd.read_csv("exported_data/world_GDP.csv")
    print(f"world_GDP\n{world_GDP.head(7)}\n")


    ## Dataset related to American countries GDP (US_GDP.csv)
    US_GDP = pd.read_csv("exported_data/US_states_GDP.csv")
    print(f"US_GDP\n{US_GDP.head(7)}\n")

    ## Dataset related to European countries GDP (European_GDP_procapite.csv)
    EU_GDP = pd.read_csv("exported_data/european_GDP_procapite.csv")
    print(f"EU_GDP\n{EU_GDP.head(7)}\n")

    ## Creation of the middle table between european_bill_byProvince.json and true.json
    with open('final_data/eur_prov_matched_bill.json', 'r', encoding='utf-8') as f:

        eur_matched = json.load(f) 
    # first ten elements of the billionaires 
    cont = 0
    print("eur_prov_matched_bill\n")
    for el in eur_matched:
        if cont <= 10:
            print(el)
            cont += 1
    print("\n")

    # Dataset related to worth bill values with scraping from Forbes (all_worth_trend_bill.json)
    with open('exported_data/all_worth_trend_bill.json', 'r', encoding='utf-8') as f:
        worth_trend = json.load(f)

    # first ten elements of the billionaires worth trend list
    cont = 0
    print("all_worth_trend_bill\n")
    for el in worth_trend:
        if cont <= 10:
            print(el,worth_trend[el])
            cont += 1

    # Dataset related to worth bill values with scraping from Forbes (all_worth_trend_bill.json)
    cont = 0
    american_bill_byProvince = {}

    for el in category_list:
        try:
            if el['state']!= None:
                if len(US_GDP[US_GDP['GeoName'] == el['state']])>0:
                    american_bill_byProvince[el['personName']] = el['state']
        except KeyError:
            continue 
    print(f"american_bill_byProvince\n{american_bill_byProvince}\n")

    eur_prov_matched_bill = eur_prov_matched_bill_refining(eur_matched)
    worth_trend = worth_trend_refining(worth_trend)
    american_bill_byProvince = american_bill_byProvince_refining(american_bill_byProvince)
    US_GDP = USA_GDP_refining(US_GDP)

    print(f"US_GDP\n{US_GDP}\n")