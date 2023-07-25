from DataAcquisition.american_gdp import american_GDP_def
from DataAcquisition.world_gdp import world_GDP_def
from DataAcquisition.european_gdp import european_GDP_def
from DataAcquisition.worth_bill import worth_trend_scraping
from DataAcquisition.billionaires_forbes import import_true, add_continent, match_fixing

if __name__ == "__main__":
    # open all the raw datasets, if you want to re-run the scraping file you have to look at data_scraping.py
    
    world_GDP = world_GDP_def()
    region_GDP = european_GDP_def()
    USA_GDP = american_GDP_def()
    
    category_list = import_true()
    add_continent(category_list, USA_GDP)

    worth_trend = worth_trend_scraping(category_list)

    category_list = match_fixing(category_list,world_GDP)

    