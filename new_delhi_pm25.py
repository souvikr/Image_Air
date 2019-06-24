#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import datetime
import csv
from time import sleep


# In[ ]:


prev_sensorTime=0
while(1):
    r=requests.get("https://www.aqi.in/live-stream")
    data1=r.text
    i1=data1.index('token')
    token=data1[i1+9:i1+357]
    autho="Bearer "+token
    print("autho= ",autho)
    headers = {
        'Accept': 'application/json',
        'Referer': 'https://www.aqi.in/live-stream',
        'Origin': 'https://www.aqi.in',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'serialNo': 'PLLODA000302',
        'Authorization': autho,
        'Content-Type': 'application/json',
    }

    response = requests.get('https://api.aqi.in/webAPI/api/protected/getDevicePage', headers=headers)

    
    data=response.json()
    
    date_r=data['timeStamp']
    frmt1='%d %b %Y,     %I:%M %p'
    frmt2='%Y_%m_%d %H_%M'
    date_r=datetime.datetime.strptime(date_r, frmt1).strftime(frmt2)
    
    pm25=data['airComponents'][1]['sensorData']
    temp=data['airComponents'][2]['sensorData']
    humd=data['airComponents'][3]['sensorData']
    PM10=data['airComponents'][5]['sensorData']
    #print(date_r,", ",sensorData,", ",cityName)
    file_name="NewDelhi/NewDelhi_PM25_records.csv"
    if date_r!=prev_sensorTime:
        with open(file_name, 'a+', newline='') as csvFile:
            writer = csv.writer(csvFile)
            # writer.writerow(["Date","sensorData"])
            writer.writerow([date_r,pm25,temp,humd,PM10])
            print(date_r,", ",pm25,", ",temp,", ",humd,", ",PM10)
            
    prev_sensorTime=date_r
    
    sleep(900)


# In[ ]:




