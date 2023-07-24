from data_acquisition import *

## Dataset related to bill characteristics (True.json)
with open('exported_data/true.json', 'r', encoding='utf-8') as f:

    category_list = json.load(f)
# first ten elements of the billionaires 
cont = 0
print("true\n")
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