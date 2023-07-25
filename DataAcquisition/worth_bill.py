from import_file import *

def worth_trend_scraping(category_list):
    # Dataset related to worth bill values with scraping from Forbes (all_worth_trend_bill.json)
    url = "https://www.forbes.com/profile/"
    worth_trend = {}

    for el in category_list:
        
        r = requests.get(url+el['uri'])
        soup = BeautifulSoup(r.content) # If this line causes an error, run 'pip install html5lib' or install html5lib
        canvas_list = soup.find_all("canvas")
            
        for i in list(canvas_list):
            json_data = json.loads(i['data-chart'])
            bill_diz = {}
            for data in json_data:
                
                index = data['date'].find(" ")
                year = data['date'][index+1:]
                def_worth = data['worth'].replace("$","")
                def_worth = def_worth.replace("B","")
                
                if int(year) >= 2014 and int(year) <= 2022:
                    bill_diz[int(year)] = float(def_worth)
            print(f"{el['personName']}-->{bill_diz}")
            
            worth_trend[el['personName']] = bill_diz
    return worth_trend
