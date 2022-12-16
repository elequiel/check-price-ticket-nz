import json, requests
from tabulate import tabulate
import os


from dotenv import load_dotenv
load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
TICKET_URL = os.getenv('TICKET_URL')

apiURL = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"

def get_prices():
    req = requests.get(TICKET_URL)
    dates = json.loads(req.text)
    days = dates["PriceGrids"]["Grid"]
    output = []
    for day in range(len(days[0])):
        if("Indirect" in days[0][day].keys()):
            item = []
            item.append(day+1)
            item.append(days[0][day]['Indirect']['Price'])
            output.append(item)
    return output

def send_message():
    prices = get_prices()
    try:
        response = requests.post(apiURL, json={'chat_id': CHAT_ID, 'text': f"{tabulate(get_prices(),headers=['Dia', 'Valor'])}"})
        return response.text
    except Exception as e:
        return print(e)

#print(get_prices())
# print(f"{tabulate(get_prices(),headers=['Dia', 'Valor'])}")
print(send_message())