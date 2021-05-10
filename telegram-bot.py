from telegram.ext import Updater, CommandHandler
import requests
import re
import json 
import datetime
import time
z={}
def main():
    x = datetime.datetime.now()
    a=x.strftime("%d")
    b=x.strftime("%m")
    c=x.strftime("%Y")
    a = a+"-"+b+"-"+c
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    new_response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date="+a,headers = headers)
    y = response.json()
    # print(y)
    if y == z:
        time.sleep(300)
        return y

    length = len(y["centers"])

    s = ""
    for i in range(length):
        if y['centers'][i]['sessions'][0]['available_capacity']>0 and y['centers'][i]['sessions'][0]['min_age_limit'] == 45:
            s+=(y["centers"][i]["name"])
            s+="\n"
            s+=(y["centers"][i]["address"])
            s+="\n"
            s+=str((y["centers"][i]["pincode"]))
            s+="\n"
            s+=(y["centers"][i]["fee_type"])
            s+="\n"
            s+=str((y['centers'][i]['sessions'][0]['available_capacity']))
            s+="\n"
            s+=str((y['centers'][i]['sessions'][0]['date']))
            s+="\n"
            s+=str((y['centers'][i]['sessions'][0]['vaccine']))
            s+="\n"
            s+="\n"

    print(s)
    requests.post("https://api.telegram.org/bot1872421161:AAGft5meCIwb8xoyv91eAk2eLbxzTyCv2mM/sendMessage?chat_id=-329970000&text="+s)
    time.sleep(300)
    return y
if __name__ == '__main__':
    try:
        while(1):
            z = main()
    except:
        exit()